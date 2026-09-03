import os
import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import MarkdownTextSplitter
from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# ============================================================
# 1. CORE PIPELINE INITIALIZATION (Cached for Performance)
# ============================================================

load_dotenv()

@st.cache_resource
def initialize_rag_pipeline():
    """Initializes the Vector DB and Gemini LLM once and caches them."""

    
    # Repository-relative paths
    persist_directory = str(BASE_DIR / "vector_db")
    sop_folder = str(BASE_DIR / "SOPs")
    
    # 1. Load Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # 2. Connect to existing Chroma DB
    vector_db = Chroma(persist_directory=persist_directory, embedding_function=embeddings)


    # Connect to Gemini Model

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash", 
        temperature=0.0,
        api_version="v1",
        max_retries=1
    )

    return vector_db, llm

# Load the single instances to reuse across all user queries
vector_db, llm = initialize_rag_pipeline()


def load_runtime_sops():
    """
    Read current SOP/reference files directly from disk.
    These files are NOT added to Chroma.
    """

    sop_folder = str(BASE_DIR / "SOPs")

    runtime_sops = []

    if not os.path.exists(sop_folder):
        return runtime_sops

    for file_name in os.listdir(sop_folder):

        if not file_name.lower().endswith((".md", ".txt")):
            continue

        file_path = os.path.join(sop_folder, file_name)

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                sop_text = f.read()

            # Try to identify the human-readable SOP/document ID
            document_id = "N/A"

            for line in sop_text.splitlines():
                stripped = line.strip()

                if "Document ID" in stripped:
                    document_id = stripped.split(":", 1)[-1].strip()
                    break

                if "SOP-" in stripped:
                    parts = stripped.split()
                    for part in parts:
                        if part.startswith("SOP-"):
                            document_id = part.strip("*#:`")
                            break

                    if document_id != "N/A":
                        break

            runtime_sops.append({
                "source_manual": file_name,
                "document_id": document_id,
                "section": "SOP Standard Rule",
                "page": "N/A - Markdown SOP",
                "text": sop_text
            })

        except Exception:
            continue

    return runtime_sops

# ============================================================
# 2. RUNTIME QUERY FUNCTION
# ============================================================
def ask_question(question, k=5, district=None, owner=None):

    """
    Ask an engineering question using Chroma + Gemini.

    Parameters:
        question: User's engineering question
        k: Number of documents to retrieve
        district: Selected Caltrans district, if applicable
        owner: Selected utility owner, if applicable

    Returns:
        answer: Generated answer text
        sources: Retrieved document metadata
    """
    # 1. Retrieve relevant documents using your cached vector_db
    retrieval_query = question

    # Add Caltrans terminology to improve retrieval when users use
    # informal terminology that differs from the source manuals.
    retrieval_query += """
    Caltrans utility encasement casing uncased pipeline
    encasement exception State highway right-of-way
    high-pressure natural gas TR-0158 UNG
    """

    if district:
        retrieval_query += f" Caltrans District {district}"

    if owner:
        retrieval_query += f" {owner}"

    # Retrieve relevant documents
    docs = vector_db.similarity_search(
        retrieval_query,
        k=k
    )

    print("\n===== RETRIEVED DOCUMENTS =====")
    for i, doc in enumerate(docs, 1):
        print(f"\n--- RETRIEVED {i} ---")
        print(f"Source: {doc.metadata.get('source_manual')}")
        print(f"Page: {doc.metadata.get('page')}")
        print(f"Section: {doc.metadata.get('section')}")
        print(doc.page_content[:1500])

    # 2. Build grounded context
    context = "\n\n".join(
        f"SOURCE: {doc.metadata.get('source_manual')}\n"
        f"PAGE: {doc.metadata.get('page')}\n"
        f"SECTION: {doc.metadata.get('section')}\n"
        f"TEXT:\n{doc.page_content}"
        for doc in docs
    )
    # 2A. Load current SOP/reference files directly from disk
    runtime_sops = load_runtime_sops()

    # Select the most relevant SOPs using the user's question
    # This is local processing only — no Gemini call.
    query_terms = {
        word.strip(".,?!:;()[]{}").lower()
        for word in retrieval_query.split()
        if len(word.strip(".,?!:;()[]{}")) >= 4
    }

    scored_sops = []

    for sop in runtime_sops:
        sop_text = sop["text"].lower()

        score = sum(
            1
            for term in query_terms
            if term in sop_text
        )

        if score > 0:
            scored_sops.append((score, sop))

    # Highest relevance first; keep the top 3
    scored_sops.sort(key=lambda x: x[0], reverse=True)
    relevant_sops = [sop for score, sop in scored_sops[:3]]

    print("\n===== SELECTED RUNTIME SOPS =====")
    for score, sop in scored_sops[:3]:
        print(
            f"Score: {score} | "
            f"File: {sop['source_manual']} | "
            f"ID: {sop['document_id']}"
        )

    # Build runtime SOP context
    runtime_sop_context = "\n\n".join(
        f"SOP DOCUMENT ID: {sop['document_id']}\n"
        f"SOURCE FILE: {sop['source_manual']}\n"
        f"PAGE: {sop['page']}\n"
        f"SECTION: {sop['section']}\n"
        f"TEXT:\n{sop['text']}"
        for sop in relevant_sops
    )

    # Combine permanent Chroma references with relevant runtime SOP references
    if runtime_sop_context:
        context += "\n\n===== CURRENT RUNTIME SOP REFERENCES =====\n\n"
        context += runtime_sop_context

# --------------------------- # 4. Build selected project context # ------------------------------------ 
    selected_context = ""
    if district: 
        selected_context += ( f"Selected Caltrans District: {district}\n" )
    if owner: 
        selected_context += ( f"Selected Utility Owner: {owner}\n" )

    with open(BASE_DIR / "prompts" / "engineering_prompt.txt", "r", encoding="utf-8") as f:
        engineering_prompt = f.read()

    # Prompt Gemini with the engineering rule framework
    prompt = f"""
{engineering_prompt}

SELECTED PROJECT CONTEXT: 
{selected_context}

USER QUESTION:
{question}

DOCUMENT CONTEXT:
{context}
"""

    # Generate answer using the cached LLM instance
    try:
        response = llm.invoke(prompt)
    except Exception as e:
        error_text = str(e)

        if "503" in error_text or "UNAVAILABLE" in error_text:
            return (
                "Gemini is temporarily unavailable due to high demand. "
                "Your documents and SOP references were retrieved successfully, "
                "but the AI response could not be generated. Please try again shortly.",
                []
            )

        raise
    # ✅ FIX: Handle the new LangChain response object safely
    if isinstance(response.content, list):
        # Extract the text string out of the Pydantic dict block
        answer = "".join([chunk.get("text", "") for chunk in response.content if isinstance(chunk, dict)])
    else:
        answer = response.content

    # Remove trailing/leading spaces
    answer = answer.strip()

    # 5. RECORD RETRIEVED SOURCES
    sources = []
    seen = set()

    # Record Chroma sources
    for doc in docs:
        source_manual = doc.metadata.get("source_manual", "Unknown")
        page = doc.metadata.get("page", "N/A")
        section = doc.metadata.get("section", "N/A")

        unique_key = ("chroma", source_manual, page, section)

        if unique_key not in seen:
            seen.add(unique_key)

            sources.append({
                "source_manual": source_manual,
                "page": page,
                "section": section,
                "document_id": "N/A",
                "source_type": "Chroma"
            })

    # Record runtime SOP sources
    for sop in relevant_sops:
        source_manual = sop.get("source_manual", "Unknown")
        document_id = sop.get("document_id", "N/A")
        page = sop.get("page", "N/A")
        section = sop.get("section", "Runtime SOP Reference")

        unique_key = ("runtime_sop", source_manual)

        if unique_key not in seen:
            seen.add(unique_key)

            sources.append({
                "source_manual": source_manual,
                "document_id": document_id,
                "page": page,
                "section": section,
                "source_type": "Runtime SOP"
            })

    return answer, sources

