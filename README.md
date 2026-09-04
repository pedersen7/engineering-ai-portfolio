# AI for Transportation & Infrastructure Engineering

**Michael Pedersen**
San Diego, California
Civil Engineering | Transportation Infrastructure | Artificial Intelligence

**25+ years of engineering experience**
**Current focus:** Computer Vision • Engineering Knowledge Systems • AI-Assisted Workflows

---

## About

I am a Civil Engineer with more than 25 years of experience delivering transportation and infrastructure projects across the United States and Australia.

I am now applying modern Artificial Intelligence and Machine Learning techniques to practical engineering problems, with a particular focus on transportation infrastructure, utility coordination, infrastructure inspection, and engineering knowledge systems.

This portfolio documents that work through working prototypes, experiments, evaluations, and lessons learned.

---

## Vision

To develop practical AI tools that can assist transportation and infrastructure engineers by combining:

* Computer vision
* Engineering knowledge retrieval
* Structured engineering workflows
* Domain-specific engineering knowledge
* Human engineering judgment

The objective is not to replace engineering judgment, but to explore how AI can make engineering information and workflows more accessible, consistent, and efficient.

---

## Featured Project

### Caltrans Utility AI Assistant

**Computer Vision | Engineering Knowledge Retrieval | AI-Assisted Engineering Workflows**

The **Caltrans Utility AI Assistant** is an independently developed engineering AI prototype exploring how computer vision, engineering knowledge retrieval, and workflow-aware AI assistance can be combined to support transportation and utility engineering.

The project brings together two complementary capabilities.

### Utility-AI — Computer Vision

A computer vision system for detecting and classifying transportation and utility infrastructure assets from field imagery.

Development includes:

* Custom infrastructure image dataset development
* Image annotation using Label Studio
* YOLO object detection
* Transfer learning
* Dataset refinement based on model failures
* Model evaluation and diagnostics
* Independent field-image evaluation
* Engineering interpretation of detection results

### Infrastructure-RAG — Engineering Knowledge

A Retrieval-Augmented Generation system designed to help engineers locate and organize relevant information from engineering references and structured engineering workflows.

Development includes:

* Semantic document retrieval using Chroma
* Engineering document and manual retrieval
* Retrieval evaluation using realistic engineering questions
* Cross-encoder reranking and retrieval diagnostics
* Engineering-specific response instructions
* Runtime selection of relevant engineering SOPs
* Caltrans District context
* Utility-owner context
* Standard and specification lookup
* Section 77 drafting workflow
* Integration of engineering reference notes
* Streamlit-based user interface

The two capabilities represent different stages of a potential engineering workflow:

```text
Field Information
       ↓
Computer Vision
       ↓
Identify Infrastructure Asset
       ↓
Engineering Context
       ↓
Knowledge Retrieval
       ↓
Engineering Analysis
       ↓
Human Review / Judgment
```

The longer-term concept is:

> **See the infrastructure → identify the asset → retrieve relevant engineering knowledge → support the engineering workflow.**

**Project status:** Active development

**[Explore the Caltrans Utility AI Assistant](Caltrans-Utility-AI-Assistant/)**

**[View the Project Presentation](Caltrans-Utility-AI-Assistant/presentation/Presentation.pdf)**

---

## Why This Work?

Infrastructure engineering involves large amounts of technical information distributed across manuals, specifications, standard plans, procedures, project documents, and institutional knowledge.

AI provides an opportunity to explore new ways of working with that information.

The Caltrans Utility AI Assistant investigates two complementary questions:

**Computer Vision**

> What can AI identify from infrastructure field imagery?

**Engineering Knowledge Systems**

> How can AI help engineers find, organize, and apply relevant technical information?

The longer-term goal is to explore how these capabilities could work together within practical engineering workflows.

---

## Engineering Lessons Learned

Several themes have emerged through the development of the project.

### Dataset quality matters

Improving annotation consistency, bounding-box quality, class definitions, and difficult examples often produced more meaningful improvements than simply increasing model complexity.

### Validation metrics are not enough

Standard validation results can look encouraging while real-world field imagery exposes weaknesses that are not apparent in the training or validation datasets.

Independent testing therefore became an important part of the development process.

### Retrieval quality matters

A RAG system can contain the correct engineering information and still fail to provide a useful answer if the relevant material is not retrieved.

This led to experimentation with:

* Query formulation
* Retrieval vocabulary
* Candidate expansion
* Reranking
* Diagnostic evaluation
* Engineering-specific retrieval testing

### Engineering context matters

AI systems operating in engineering environments need more than general language capability.

They need appropriate engineering context, source references, workflow awareness, and clear distinctions between documented requirements, alternatives, assumptions, and engineering judgment.

---

## Current Research Areas

* AI-assisted utility and transportation asset detection
* Engineering knowledge retrieval using RAG
* Utility coordination workflows
* Infrastructure inspection
* Engineering document analysis
* AI-assisted technical decision support
* Computer vision and engineering knowledge-system integration
* GIS and spatial-analysis concepts

---

## Technology

**Artificial Intelligence / Machine Learning**

* Python
* YOLO
* Computer Vision
* Object Detection
* Transfer Learning
* Retrieval-Augmented Generation (RAG)
* Large Language Models

**Engineering / Data**

* Transportation Engineering
* Utility Engineering
* Infrastructure Asset Management
* GIS
* Engineering Document Retrieval
* Dataset Development
* Model Evaluation

**Development Tools**

* Streamlit
* LangChain
* Chroma
* Hugging Face
* OpenCV
* Label Studio
* Google Colab
* VS Code
* Git / GitHub

---

## Portfolio Structure

```text
engineering-ai-portfolio/
│
├── README.md
│
├── Caltrans-Utility-AI-Assistant/
│   ├── README.md
│   │
│   ├── presentation/
│   │   ├── README.md
│   │   └── Presentation.pdf
│   │
│   ├── Utility-AI/
│   │   ├── README.md
│   │   ├── docs/
│   │   ├── images/
│   │   └── YOLO_Model_Evaluation/
│   │
│   └── Infrastructure-RAG/
│       ├── README.md
│       ├── docs/
│       ├── app.py
│       ├── core_rag.py
│       └── requirements.txt
│
├── resume/
│
├── .gitignore
└── LICENSE
```

Private engineering manuals, SOPs, vector databases, model weights, prompts, and project-specific reference material are intentionally excluded from the public repository.

The portfolio provides the overall engineering and AI context, while the **Caltrans Utility AI Assistant** contains the detailed technical documentation and development history.

---

## Future Direction

Future development will explore deeper integration of computer vision and engineering knowledge systems into a unified infrastructure engineering workflow.

Potential areas include:

* Combining field-image asset detection with engineering knowledge retrieval
* Expanding engineering workflow support
* Additional infrastructure and utility standards
* GIS integration
* Improved retrieval and evaluation methods
* Field-oriented engineering assistance

The emphasis will remain on **practical engineering applications, transparent evaluation, and responsible use of AI**.

---

## Professional Background

My professional background includes transportation engineering, utilities, environmental engineering, water resources, construction, project management, GIS, and infrastructure delivery.

This engineering experience provides the domain context for the AI projects documented in this portfolio.

📄 **Resume:** [Michael_Pedersen_Resume.pdf](resume/Michael_Pedersen_Resume.pdf)

---

## GitHub

[View my GitHub projects](https://github.com/pedersen7)

---

*This portfolio documents ongoing independent exploration of Artificial Intelligence applied to transportation and infrastructure engineering.*

