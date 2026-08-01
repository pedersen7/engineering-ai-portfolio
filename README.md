
# Engineering AI Portfolio

**Location:** San Diego, California  
**Background:** Civil Engineering | Transportation Infrastructure  
**Experience:** 25+ Years  
**Current Focus:** Computer Vision • AI • Engineering Knowledge Systems

Welcome! I'm Michael Pedersen, a Civil Engineer with over 25 years of experience delivering transportation and infrastructure projects across the United States and Australia.  
I'm currently expanding my engineering expertise into Artificial Intelligence by developing computer vision applications for transportation infrastructure, utility coordination, and engineering decision support.  

## Professional Links

📄 **Resume:** [Michael_Pedersen_Resume.pdf](resume/Michael_Pedersen_Resume.pdf)  (PDF)
💼 **GitHub:** https://github.com/pedersen7

---

## Project Highlights

- Developed a custom computer vision dataset for transportation and utility infrastructure.
- Designed an iterative annotation and model improvement workflow using Label Studio and YOLO11.
- Reduced the original 34-class taxonomy to a refined 21-class engineering dataset.
- Implemented transfer learning and repeated model evaluation using Google Colab.
- Established an independent field test methodology using unseen roadway imagery.
- Applied transportation engineering domain knowledge to the development of AI-assisted infrastructure inspection workflows.

## Why This Project?

This project combines over 25 years of transportation engineering experience with modern computer vision techniques to explore how AI can assist engineers in locating and identifying utility infrastructure from ordinary field imagery.

Rather than focusing solely on benchmark accuracy, the project emphasizes iterative dataset refinement, engineering judgment, and evaluation using independent real-world field images.

---

## Current Project

The objective is not only to maximize validation metrics, but to develop a practical engineering tool capable of reliable performance on previously unseen field imagery.

### AI-Assisted Utility Asset Detection

_This project explores the application of computer vision to automate the detection and classification of transportation and utility infrastructure assets from field imagery._

Current areas of development include:

- Custom dataset development
- Image annotation using Label Studio
- YOLO object detection
- Model training and evaluation
- Engineering workflow integration
- GIS integration concepts

The source code and datasets remain private while the project is under active development. Project documentation and development progress are shared through this repository.

This repository documents the ongoing development of an AI engineering project that combines transportation engineering expertise with modern computer vision techniques.

Additional projects and technical documentation will be added over time.

Field Images -:> Annotation -:> YOLO Training -:> Evaluation -:> Performance Review -:> Dataset Improvement

<img width="258" height="447" alt="Untitled" src="https://github.com/user-attachments/assets/f4429273-19a5-4e78-85e3-d5e95d1fd19a" />

_The workflow follows an iterative engineering process where model evaluation informs dataset refinement, resulting in progressively improved model performance._

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

### Short Term

- Continue targeted data collection
- Expand hard test benchmark
- Improve small-object detection
- Additional model comparison studies

### Medium Term

- Mobile inference workflow
- Retrieval-Augmented Generation (RAG)
- GIS integration

### Long Term

- AI-assisted infrastructure inspection platform
- Engineering knowledge assistant
  
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

## Repository Structure
```text
Engineering-AI-Portfolio/
│
├── README.md                    # Project overview
├── LICENSE
│
├── docs/
│   ├── Project_Overview.md
│   ├── Dataset.md
│   ├── Annotation_Process.md
│   ├── Model_Training.md
│   ├── Model_Evaluation.md
│   ├── Version_History.md
│   ├── Lessons_Learned.md
│   ├── Roadmap.md
│   └── Engineering_Decisions.md
│
├── images/
│   ├── workflow.png
│   ├── annotation_example.png
│   ├── training_results.png
│   ├── confusion_matrix.png
│   ├── sample_detection.png
│   └── dataset_examples.png
│
├── resume/
│   └── Michael_Pedersen_Resume.pdf
│
├── notebooks/
│
├── scripts/
│
└── .gitignore


