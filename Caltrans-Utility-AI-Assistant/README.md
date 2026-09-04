# Caltrans Utility AI Assistant

An independently developed engineering AI prototype exploring how **computer vision, engineering knowledge retrieval, and workflow-aware AI assistance** can be combined to support transportation and utility engineering.

## Overview

The **Caltrans Utility AI Assistant** explores how modern Artificial Intelligence and Machine Learning techniques can be applied to practical engineering tasks involving transportation infrastructure, utilities, engineering requirements, and field information.

The project brings together two complementary AI capabilities:

### 1. Utility-AI — Computer Vision

A computer vision system for detecting and classifying transportation and utility infrastructure assets from field imagery.

The work includes:

* Custom infrastructure image dataset development
* Image annotation and dataset refinement
* YOLO object detection
* Transfer learning
* Model evaluation and diagnostics
* Independent field-image testing
* Engineering interpretation of detection results

### 2. Infrastructure-RAG — Engineering Knowledge

A Retrieval-Augmented Generation system designed to help engineers locate and organize relevant technical information from engineering references.

The system includes:

* Semantic document retrieval
* Chroma vector database
* Embeddings and cross-encoder reranking
* Engineering-specific prompt architecture
* Engineering workflow and SOP integration
* Caltrans District context
* Utility-owner context
* Structured engineering responses
* Source and page references
* Retrieval evaluation and diagnostics
* Streamlit interface

## The Engineering AI Concept

The two components represent different stages of a potential engineering workflow:

```text
                 FIELD INFORMATION
                       |
                       v
                Computer Vision
                       |
                       v
                 Identify Asset
                       |
                       v
              Engineering Context
                       |
                       v
             Knowledge Retrieval
                       |
                       v
             Engineering Analysis
                       |
                       v
              Engineering Workflow
                       |
                       v
             Human Review / Judgment
```

The longer-term concept is:

> **See the infrastructure → identify the asset → retrieve relevant engineering knowledge → support the engineering workflow.**

The goal is not to replace engineering judgment. The system is intended to explore how AI can help engineers access information, organize technical knowledge, and support repetitive or information-intensive engineering tasks.

## Why This Project?

Transportation and utility engineering involves large amounts of technical information distributed across:

* Engineering manuals
* Standard specifications
* Procedures
* Utility requirements
* Project documentation
* Historical engineering knowledge
* Field observations

At the same time, field conditions often provide the starting point for engineering decisions.

This project explores the potential connection between **what can be observed in the field** and **what engineering knowledge is needed to interpret or act on that information**.

## Evaluation and Development

The project has been developed through iterative testing rather than relying solely on demonstrations.

### Computer Vision

Model development has included:

* Training and validation metrics
* Precision, recall, and F1 analysis
* Confusion-matrix analysis
* Representative validation predictions
* Independent field-image evaluation
* Dataset refinement based on observed model weaknesses

### Engineering RAG

The RAG system has been evaluated using realistic engineering questions, including:

* Relevant-page identification
* Retrieval accuracy
* Candidate expansion
* Cross-encoder reranking
* Retrieval diagnostics
* Difficult and ambiguous questions
* Engineering response quality
* Source verification

A major development lesson has been that **AI system performance depends on more than the underlying model**.

Dataset quality, retrieval quality, engineering context, workflow logic, source material, and human evaluation all contribute to the usefulness of the system.

## Engineering Knowledge and Responsible AI

The working engineering environment contains additional material that is intentionally excluded from this public repository.

Private material may include:

* Full engineering manuals
* Engineering notes
* Detailed SOPs
* Project-specific workflows
* Internal prompts and configuration
* Vector database contents
* Proprietary or project-specific reference material
* API credentials

The public repository therefore demonstrates the **technical architecture, implementation approach, evaluation methodology, and development process** without publishing private or project-specific engineering information.

The system is an **engineering-assistance prototype** and does not replace applicable agency requirements, project-specific verification, field investigation, or qualified engineering judgment.

## Project Structure

```text
Caltrans-Utility-AI-Assistant/
│
├── README.md
│
├── presentation/
│   ├── README.md
│   └── Presentation.pdf
│
├── Utility-AI/
│   ├── docs/
│   ├── images/
│   └── YOLO_Model_Evaluation/
│
└── Infrastructure-RAG/
    ├── docs/
    ├── app.py
    ├── core_rag.py
    ├── README.md
    └── requirements.txt
```

Each component contains more detailed documentation and supporting material.

## Project Resources

### Project Presentation

A visual overview of the project, development process, evaluation, lessons learned, and future direction.

**[View the Project Presentation](presentation/)**

### Utility-AI

Computer vision development, documentation, model evaluation, and representative results.

**[Explore Utility-AI](Utility-AI/)**

### Infrastructure-RAG

RAG architecture, application code, retrieval methodology, evaluation, and technical documentation.

**[Explore Infrastructure-RAG](Infrastructure-RAG/)**

## Future Direction

The current system establishes a foundation for deeper integration between field information, engineering knowledge, and engineering workflows.

Potential future development includes:

* Connecting detected assets directly to engineering knowledge retrieval
* Photo-based engineering analysis
* Live field detection
* GIS and spatial context
* Additional utility-owner knowledge
* Supplemental engineering guidance
* Expanded engineering workflow support
* Improved retrieval and evaluation methods
* Pavement and roadway condition detection
* Multi-step engineering workflow orchestration

The direction is not simply **more AI**.

It is deeper integration between:

> **Engineering knowledge + project context + field information + AI-assisted workflows + human engineering judgment**

## Project Status

**Active development / engineering AI prototype**

This project represents ongoing independent exploration of Artificial Intelligence and Machine Learning applied to transportation and infrastructure engineering.

---

*Caltrans Utility AI Assistant is an independently developed prototype and is not an official Caltrans product or system.*

