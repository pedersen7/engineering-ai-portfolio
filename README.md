
# AI for Transportation & Infrastructure Engineering

**Location:** San Diego, California  
**Background:** Civil Engineering | Transportation Infrastructure  
**Experience:** 25+ Years  
**Current Focus:** Computer Vision • AI • Engineering Knowledge Systems

Welcome! I'm Michael Pedersen, a Civil Engineer with over 25 years of experience delivering transportation and infrastructure projects across the United States and Australia.  
I'm currently expanding my engineering expertise into Artificial Intelligence by developing computer vision applications for transportation infrastructure, utility coordination, and engineering decision support.  

# Vision

To develop practical AI tools that assist transportation and infrastructure engineers by combining computer vision, engineering knowledge retrieval, and structured engineering workflows.

## Professional Links

📄 **Resume:** [Michael_Pedersen_Resume.pdf](resume/Michael_Pedersen_Resume.pdf)  (PDF)
💼 **GitHub:** https://github.com/pedersen7

## Current Research Areas

- AI-assisted utility asset detection using computer vision
- Engineering knowledge retrieval using Retrieval-Augmented Generation (RAG)
- Practical AI workflows for transportation and infrastructure engineering

---

## Project Highlights

- Developed a custom computer vision dataset for transportation and utility infrastructure.
- Designed an iterative annotation and model improvement workflow using Label Studio and YOLO11.
- Reduced the original 34-class taxonomy to a refined 21-class engineering dataset.
- Implemented transfer learning and repeated model evaluation using Google Colab.
- Established an independent field test methodology using unseen roadway imagery.
- Applied transportation engineering domain knowledge to the development of AI-assisted infrastructure inspection workflows.

## Why This Portfolio?

modern Artificial Intelligence techniques. Current projects explore how computer vision and engineering knowledge systems can assist engineers with infrastructure inspection, utility coordination, and technical decision support.

Rather than focusing solely on benchmark accuracy, these projects emphasize practical engineering workflows, iterative improvement, and the application of AI to real-world transportation and infrastructure challenges.

---

## Featured Projects

### AI-Assisted Utility Asset Detection - Computer Vision

Detect and classify utility and transportation infrastructure from field imagery using YOLO.

This project explores the application of computer vision to automate the detection and classification of transportation and utility infrastructure assets from field imagery.

Current areas of development include:

- Custom dataset development
- Image annotation using Label Studio
- YOLO object detection
- Model training and evaluation
- Engineering workflow integration
- GIS integration concepts

**Status**
- Version 3 Complete
- Version 4 Planning

Field Images -:> Annotation -:> YOLO Training -:> Evaluation -:> Performance Review -:> Dataset Improvement

Field Collection
        │
        ▼
Image Annotation
        │
        ▼
Dataset Refinement
        │
        ▼
YOLO Training
        │
        ▼
Validation Metrics
        │
        ▼
Independent Field Testing
        │
        ▼
Failure Analysis
        │
        ▼
Targeted Dataset Improvements

<img width="258" height="447" alt="Untitled" src="https://github.com/user-attachments/assets/f4429273-19a5-4e78-85e3-d5e95d1fd19a" />

_The workflow follows an iterative engineering process where model evaluation informs dataset refinement, resulting in progressively improved model performance._

---

## Infrastructure Knowledge Assistant (RAG)

Developing an engineering knowledge assistant using Retrieval-Augmented Generation (RAG) to help engineers navigate technical manuals, workflows, and engineering guidance.

Current work includes:

document retrieval
vector databases
engineering workflow integration
evaluation using realistic engineering questions

**Status**

- Proof of concept

---

## Current Status

Version 3 Complete (Initial Release)

Current focus has shifted from increasing validation metrics to improving
real-world performance using an independent field test set.

Recent achievements include:

- Refined annotation consistency
- Improved bounding box quality
- Transfer learning from the best Version 2 model
- Expanded dataset with difficult and negative examples
- Established an independent unseen field test benchmark
- Identified remaining challenges involving small, low-contrast utility assets

The project now evaluates models using both standard validation metrics and an independent field test set, providing a more realistic assessment of real-world performance.


Version 1 Complete

- 270 field images
- 772 annotated utility assets  
- 34 original classes  
- Initial YOLO11n model trained and evaluated
- Baseline established for Version 2 improvements

Version 2/2.1 Complete

- Dataset refinement and better distribution on some features, like water valve lids
- Class consolidation, improved annotations, larger dataset
- Additional field data collection
- Simplified to 21 classes
- Fine tuned model
- Expanded unseen testing
- 462 images, trained 369, valid 93 (395 objects), classes 21
- Rebalanced, 462 images, trained 359, valid 103

---

## Dataset Snapshot

Current Development

- 460+ field images
- 21 infrastructure asset classes
- 1,000+ manually annotated utility assets
- Multiple dataset refinement cycles
- Independent unseen field evaluation benchmark

---

## Project Gallery

<table>
<tr>
<td align="center">
<b>Annotation</b><br>
<img width="350" height="501" alt="Untitled" src="https://github.com/user-attachments/assets/b7e3c04b-a11b-47ce-90dc-c207afc90568" />
</td>

<td align="center">
<b>Training Results</b><br>
<img width="350" alt="Screenshot 2026-07-11 164540" src="https://github.com/user-attachments/assets/e5b66312-7290-422e-9074-06fedf414ae9" />
</td>
</tr>

<tr>
<td align="center">
<b>Confusion Matrix</b><br>
<img width="350" alt="Screenshot 2026-07-11 164656" src="https://github.com/user-attachments/assets/d8d7eb4f-2de0-4885-93bf-8b6e4eaf10ea" />
</td>

<td align="center">
<b>Detection Example</b><br>
<img width="344" height="523" alt="Screenshot 2026-07-11 162946" src="https://github.com/user-attachments/assets/84062b95-abd7-4c03-8545-0c6a941a6679" />
</td>
</tr>
</table>


---

## Engineering Lessons Learned

- Dataset quality consistently produced larger improvements than increasing model complexity.
- Consistent annotation standards were critical for reliable training.
- Class taxonomy significantly affected detection performance.
- Independent field testing revealed limitations not visible through validation metrics alone.
- Model failures are now used to guide targeted dataset expansion.

---

## Future Roadmap

## AI-Assisted Utility Asset Detection
- Improve difficult classes
- Expand evaluation
- V4

## Infrastructure Knowledge Assistant
- Engineering question library
- Workflow integration
- Additional manuals
- Assistant prototype

## Future
- Combine Computer Vision and RAG
- Interactive Engineering Assistant
- GIS integration
  
---

## Technologies

- Python
- YOLO11
- TensorFlow
- OpenCV
- Label Studio
- Google Colab
- Git
- GitHub
- VS Code

- Computer Vision
- Transfer Learning
- Object Detection
- Dataset Development
- Model Evaluation

---

## Professional Interests

- Computer Vision
- Artificial Intelligence
- Transportation Engineering
- GIS & Spatial Analysis
- Utility Coordination
- Infrastructure Asset Management
- Engineering Knowledge Systems

---

## Portfolio Structure

This repository provides an overview of my AI projects focused on transportation and infrastructure engineering.

```text
Engineering-AI-Portfolio/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── Infrastructure-RAG/
│   ├── data/
│   ├── README.md
│   └── requirements.txt
│
└── Utility-AI/
    ├── docs/
    └── images/

