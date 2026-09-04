# Utility-AI — Computer Vision

The **Utility-AI** component of the Caltrans Utility AI Assistant explores the use of computer vision and machine learning to identify transportation and utility infrastructure assets from field imagery.

The objective is to develop an AI-assisted capability that can recognize infrastructure assets and provide a starting point for subsequent engineering analysis.

## Overview

The computer vision workflow includes:

* Infrastructure image collection
* Image annotation and dataset development
* Dataset refinement and quality control
* YOLO object detection
* Transfer learning
* Model training and validation
* Performance evaluation
* Independent field-image testing
* Analysis of model strengths and weaknesses

The current model development focuses on identifying a range of transportation and utility infrastructure assets from images.

## Development Approach

Model development has been iterative. Dataset improvements have included correcting annotation inconsistencies, tightening bounding boxes, adding difficult examples, and incorporating background/negative imagery.

This approach recognizes that model performance depends not only on the machine-learning architecture, but also on the quality, balance, and representativeness of the training data.

The model has been evaluated using both quantitative performance metrics and visual inspection of predictions.

## Model Evaluation

Representative results from the latest model evaluation are provided in:

**[YOLO Model Evaluation](YOLO_Model_Evaluation/)**

The evaluation includes:

* Training and validation metrics
* Precision and recall
* F1 performance
* Confusion matrices
* Class-level performance
* Representative validation predictions

The evaluation results are intended to demonstrate the development and testing process rather than imply that the model is production-ready.

## Engineering Application

Computer vision is only one part of the broader **Caltrans Utility AI Assistant** concept.

The longer-term objective is to connect asset detection with engineering knowledge retrieval and project context:

```text
Field Image
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
```

For example, an identified utility asset could eventually be used to help retrieve relevant engineering requirements, procedures, utility-owner information, or supplemental engineering guidance.

## Project Context

Utility-AI is designed to work alongside the **Infrastructure-RAG** component of the overall project.

Together, the two components explore a broader engineering workflow:

> **See the infrastructure → identify the asset → retrieve relevant engineering knowledge → support engineering analysis.**

The current implementation keeps these capabilities as separate components while establishing a foundation for future integration.

## Responsible Use

The model is an **engineering-assistance prototype**.

Computer vision detections should be treated as an aid to field identification and not as a substitute for field verification, applicable engineering requirements, or qualified engineering judgment.

## Project Status

**Active development / engineering AI prototype**

The project continues to explore improvements in dataset development, model performance, field-image testing, and integration with engineering knowledge systems.

---

*Caltrans Utility AI Assistant is an independently developed prototype and is not an official Caltrans product or system.*
