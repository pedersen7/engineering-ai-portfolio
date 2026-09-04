# Infrastructure Engineering RAG Assistant

An AI-assisted engineering knowledge retrieval system designed to help transportation and utility engineers navigate technical requirements, engineering procedures, and utility permit information.

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) workflow for engineering applications.

The system combines:

* Engineering document retrieval
* Semantic vector search
* Cross-encoder reranking
* Large language model reasoning
* Engineering-specific prompts and workflows
* Source and page references
* Structured engineering responses

The goal is not to replace engineering judgment. Instead, the system is designed to help an engineer locate relevant information and organize it into a useful engineering response.

## System Architecture

```text
Engineering Documents
        |
        v
Document Processing
        |
        v
Chunking + Metadata
        |
        v
Vector Database
        |
        v
Semantic Retrieval
        |
        v
Cross-Encoder Reranking
        |
        v
Engineering Prompt
        |
        v
Large Language Model
        |
        v
Engineering Finding
+ Requirements
+ References
+ Engineering Guidance
```

## Engineering Application

The current implementation focuses on transportation and utility engineering, including:

* Utility encroachment permits
* State highway right-of-way requirements
* Utility installation requirements
* Utility crossings
* Engineering workflows
* Technical manual retrieval
* Engineering decision support

The system has been tested using realistic engineering questions rather than only generic RAG examples.

## Evaluation

The retrieval system was evaluated using a structured set of engineering questions.

Evaluation included:

* Retrieval accuracy
* Relevant-page identification
* Reranking performance
* Engineering response quality
* Source verification
* Difficult and ambiguous engineering questions

The evaluation process was used to identify weaknesses in retrieval and improve the system iteratively.

## Current Implementation

The application includes:

* Streamlit user interface
* Persistent Chroma vector database
* Hugging Face embeddings
* Cross-encoder reranking
* Google Gemini language model
* Engineering-specific prompt architecture
* District context
* Engineering response structure
* Source and page references

## Engineering Knowledge Architecture

The production version contains additional engineering knowledge, procedures, prompts, and reference material that are intentionally not included in this public repository.

This separation allows the repository to demonstrate the technical architecture without publishing proprietary or project-specific engineering content.

## Public vs. Private Components

### Public

The public repository demonstrates:

* RAG application architecture
* Python implementation
* Retrieval and reranking approach
* Application interface
* Evaluation methodology
* Project documentation

### Private

The working engineering environment contains:

* Full engineering manuals
* Engineering notes
* Proprietary workflow information
* Engineering SOPs
* Detailed prompts
* Vector database contents
* Project-specific configuration
* API credentials

These materials remain outside the public repository.

## Technologies

* Python
* LangChain
* Chroma
* Hugging Face
* Sentence Transformers
* Cross-Encoder Reranking
* Google Gemini
* Streamlit
* Jupyter
* Git
* GitHub

## Relationship to the Engineering AI Portfolio

This project is part of the broader:

**AI for Transportation & Infrastructure Engineering**

portfolio.

The portfolio explores two complementary AI applications:

1. Computer vision for infrastructure asset detection
2. Retrieval-augmented generation for engineering knowledge systems

The longer-term objective is to explore how these technologies can work together to support practical engineering workflows.

## Status

Active development.

The current focus is improving retrieval quality, engineering workflow integration, evaluation, and presentation of the system as a practical engineering AI prototype.
