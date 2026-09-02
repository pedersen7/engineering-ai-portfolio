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

## Featured Projects

### AI-Assisted Utility Asset Detection

**Computer Vision | YOLO | Infrastructure Inspection**

A computer vision system for detecting and classifying transportation and utility infrastructure assets from field imagery.

The project began with a 34-class dataset and evolved through multiple cycles of annotation refinement, class consolidation, dataset balancing, transfer learning, and independent field testing.

**Current capabilities and research include:**

* Custom infrastructure image dataset development
* Image annotation using Label Studio
* YOLO object detection
* Transfer learning
* Dataset refinement based on model failures
* Independent field-image evaluation
* Engineering interpretation of detection results
* Exploration of GIS and infrastructure workflow integration

**Project status:** Active development

[View the Utility AI project](utility-ai/)

---

### Infrastructure Knowledge Assistant

**Retrieval-Augmented Generation (RAG) | Engineering Knowledge Systems**

A working prototype exploring how Retrieval-Augmented Generation can help engineers navigate technical manuals, engineering requirements, standard provisions, and structured engineering workflows.

The system combines document retrieval, engineering-specific prompts, structured Standard Operating Procedures, and a Streamlit interface to provide context-aware engineering assistance.

**Current capabilities include:**

* Semantic document retrieval using Chroma
* Engineering document and manual retrieval
* Retrieval evaluation using realistic engineering questions
* Reranking experiments and retrieval diagnostics
* Engineering-specific response instructions
* Runtime selection of relevant engineering SOPs
* Caltrans District context
* Utility-owner context
* Standard and specification lookup
* Section 77 drafting workflow
* Integration of engineering reference notes
* Computer-vision / engineering workflow integration
* Streamlit-based user interface

The project emphasizes **traceable engineering information and appropriate use of source material**, rather than treating the language model as an independent source of engineering authority.

**Project status:** Working prototype / active development

[View the Infrastructure RAG project](infrastructure-RAG/)

---

## Why This Work?

Infrastructure engineering involves large amounts of technical information distributed across manuals, specifications, standard plans, procedures, project documents, and institutional knowledge.

AI provides an opportunity to explore new ways of working with that information.

These projects investigate two complementary approaches:

**Computer Vision**

> What can AI identify from infrastructure field imagery?

**Engineering Knowledge Systems**

> How can AI help engineers find, organize, and apply relevant technical information?

The longer-term goal is to explore how these capabilities could work together within practical engineering workflows.

---

## Engineering Lessons Learned

Several themes have emerged through the development of these projects.

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
├── infrastructure-RAG/
│   ├── app.py
│   ├── core_rag.py
│   ├── prompts/
│   ├── SOPs/
│   ├── reference/
│   ├── documents/
│   ├── evaluation/
│   └── ...
│
├── utility-ai/
│   ├── docs/
│   ├── images/
│   └── ...
│
├── notebooks/
├── scripts/
└── resume/
```

The portfolio provides the overall engineering and AI context, while each project contains its own technical documentation and development history.

---

## Future Direction

Future development will explore the integration of computer vision and engineering knowledge systems into a unified infrastructure engineering workflow.

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
