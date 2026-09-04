# RAG System Architecture

## Overview

The Infrastructure Engineering RAG Assistant is a Retrieval-Augmented Generation (RAG) system designed to support transportation and utility engineering workflows.

The system combines semantic document retrieval, cross-encoder reranking, engineering-specific context, structured prompts, and a large language model to produce traceable engineering-oriented responses.

The system is designed as an **engineering information retrieval and decision-support tool**, not as an independent source of engineering authority.

Engineering judgment and verification of source requirements remain essential.

---

## System Architecture

The overall workflow is:

```text
Engineering Reference Documents
            |
            v
      Document Processing
            |
            v
      Chunking + Metadata
            |
            v
      Embedding Generation
            |
            v
       Chroma Vector DB
            |
            v
    Semantic Candidate Retrieval
            |
            v
    Cross-Encoder Reranking
            |
            v
      Relevant Context
            |
            +------ Engineering Context
            |       - District
            |       - Utility Owner
            |       - Workflow
            |       - SOP / Reference Guidance
            |
            v
    Engineering-Specific Prompt
            |
            v
       Gemini LLM
            |
            v
 Structured Engineering Response
            |
            v
 References + Source Information
```

---

## Document Processing

Engineering reference documents are processed before being added to the retrieval system.

The document-processing workflow includes:

* PDF loading
* Text extraction
* Document chunking
* Metadata assignment
* Embedding generation
* Vector database storage

Document metadata is used to provide additional context during retrieval and to help identify the source of retrieved information.

The production knowledge base contains engineering reference material that is intentionally excluded from this public repository.

---

## Chunking and Metadata

Documents are divided into retrieval-oriented chunks rather than being supplied to the language model as complete documents.

The system uses overlapping chunks to help preserve context across document boundaries.

Metadata can include information such as:

* Source document
* Document type
* Engineering discipline
* Section
* Topic or tags
* Page information

This metadata provides additional information that can be used when evaluating and presenting retrieved material.

---

## Embeddings and Vector Search

The system uses Hugging Face sentence-transformer embeddings to convert document chunks and user queries into numerical representations.

These representations are stored in a persistent Chroma vector database.

When a user submits a question:

1. The question is converted into an embedding.
2. The vector database searches for semantically similar document chunks.
3. A larger candidate set is retrieved for further evaluation.
4. The candidate documents are passed to the reranking stage.

This separates the initial high-recall retrieval stage from the more selective relevance-ranking stage.

---

## Cross-Encoder Reranking

Initial vector similarity provides an efficient method for identifying potentially relevant documents, but semantic similarity alone does not always identify the most useful engineering passage.

The system therefore uses a cross-encoder reranker.

The retrieval process can be summarized as:

```text
User Question
      |
      v
Vector Search
      |
      v
Candidate Documents
      |
      v
Cross-Encoder Reranker
      |
      v
Highest-Relevance Context
```

The reranking stage was introduced to improve the quality of the final context supplied to the language model.

This became an important part of the evaluation process because some engineering questions contain terminology where several documents may appear semantically similar even though only a subset directly addresses the question.

---

## Engineering Context

The system incorporates contextual information in addition to the user's question.

Examples include:

* Caltrans District
* Utility owner
* Engineering discipline
* Workflow context
* Relevant engineering procedure
* Applicable reference material

For example, the Streamlit application provides a Caltrans District selector that can be used to provide district context to the engineering workflow.

The purpose of this context is to help constrain retrieval and response generation to the circumstances relevant to the engineering task.

---

## Engineering-Specific Prompting

The language model is not given unrestricted instructions to answer engineering questions from general knowledge.

Instead, the application uses engineering-specific prompting to establish how retrieved information should be interpreted and presented.

The prompt architecture is designed to encourage:

* Use of retrieved source material
* Clear identification of requirements
* Separation of documented information from assumptions
* Appropriate use of engineering context
* Source and page references
* Recognition of uncertainty
* Avoidance of unsupported engineering claims

The detailed production prompts are intentionally excluded from the public repository.

---

## Runtime Engineering Workflows

The application supports more than simple question answering.

The broader system includes workflows for tasks such as:

* Engineering information retrieval
* Utility coordination
* Technical requirement lookup
* Standard and specification research
* Section 77 drafting assistance
* Engineering reference-note integration
* Photo-based infrastructure analysis

Some workflows use additional engineering procedures and reference material that remain in the private development environment.

---

## Source and Reference Handling

Traceability is an important design objective.

Where possible, retrieved information is associated with its source document and page information so that an engineer can verify the underlying material.

The system is therefore intended to support a workflow of:

```text
AI-Assisted Retrieval
        |
        v
Relevant Engineering Information
        |
        v
Source Identification
        |
        v
Engineer Verification
        |
        v
Engineering Decision
```

The system does not treat the language model's generated response as the authoritative engineering source.

---

## Evaluation

The retrieval system was evaluated using a structured set of realistic engineering questions.

Evaluation focused on areas including:

* Retrieval relevance
* Expected-page identification
* Candidate retrieval
* Reranking performance
* Difficult questions
* Ambiguous questions
* Engineering response quality
* Source verification

The evaluation process included diagnostic analysis of retrieval results rather than relying solely on the language model's final answer.

This helped identify cases where:

* The correct document existed but was not retrieved
* Relevant material was retrieved but ranked too low
* Multiple passages were technically related but differed in relevance
* Questions required engineering context beyond simple semantic similarity

---

## Development Approach

The system was developed iteratively.

Major development areas included:

1. Establishing a baseline RAG pipeline
2. Testing document chunking and metadata
3. Evaluating semantic retrieval
4. Expanding the candidate retrieval set
5. Adding cross-encoder reranking
6. Developing retrieval diagnostics
7. Incorporating engineering context
8. Developing structured engineering prompts
9. Adding workflow-specific capabilities
10. Testing the system against realistic engineering questions

The development process emphasized measurement and iteration rather than assuming that a technically functional RAG pipeline would automatically provide reliable engineering results.

---

## Public and Private Architecture

The public GitHub repository contains the software architecture and implementation needed to demonstrate the project.

The private development environment contains additional materials, including:

* Engineering manuals
* Project-specific reference documents
* Engineering SOPs
* Detailed engineering prompts
* Engineering reference notes
* Vector database contents
* Model files
* Project-specific configuration

These materials are intentionally excluded from the public repository.

This separation allows the technical approach to be demonstrated without publishing proprietary or project-specific engineering information.

---

## Current Limitations

The system remains a prototype and has several limitations.

These include:

* Retrieval quality depends on the underlying document collection.
* Similarity search can retrieve technically related but less relevant material.
* Reranking improves candidate selection but does not guarantee correctness.
* Language-model responses still require engineering review.
* Source documents may contain conflicting, superseded, or context-dependent requirements.
* The public repository does not contain the production engineering knowledge base.

These limitations are particularly important in engineering applications where incorrect interpretation can have practical consequences.

---

## Future Development

Potential future development includes:

* Further retrieval and reranking optimization
* Expanded evaluation datasets
* Improved source verification
* Additional engineering workflows
* GIS and spatial integration
* Integration with infrastructure asset detection
* Additional document and standards support
* Improved field-oriented engineering assistance

A longer-term objective is to explore how computer vision and engineering knowledge retrieval could operate together within a unified infrastructure engineering workflow.

---

## Technology Stack

The current implementation uses technologies including:

* Python
* Streamlit
* LangChain
* Chroma
* Hugging Face Sentence Transformers
* Cross-Encoder Reranking
* Google Gemini
* PyPDF
* Jupyter
* Git
* GitHub

---

## Engineering Philosophy

The project is based on a simple principle:

> AI should assist the engineer in finding and organizing information, while the engineer remains responsible for interpretation, verification, and judgment.

The objective is therefore not simply to build a chatbot that produces plausible answers.

The objective is to develop an AI-assisted engineering system that can:

* Retrieve relevant information
* Provide useful engineering context
* Identify supporting sources
* Expose uncertainty
* Support repeatable workflows
* Allow the engineer to verify the underlying information

