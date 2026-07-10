Problem: Detect utility infrastructure from field imagery.
Version 1: Build the complete pipeline and establish a baseline.
Version 2: Improve the dataset through class refinement and targeted data collection.
Future: Integrate RAG and GIS to create an AI-assisted utility inspection system.

Utility AI Project – Current Status
Version 1 Complete ✅

The first end-to-end object detection model has been successfully completed.

Dataset
270 annotated field images
772 annotated utility assets
34 initial classes
Annotated using Label Studio
Model
YOLO11n
Trained using Google Colab
Initial evaluation completed
Initial Findings

The model successfully detects many common utility assets including:

Distribution poles
Transmission poles
Streetlights
Telecom pedestals
Sewer manhole lids
Water valve lids

Areas identified for improvement include:

Class imbalance
Confusion between visually similar assets
Limited examples for rare classes
Refinement of class taxonomy
Version 2 Objectives
Merge visually similar classes
Remove extremely rare classes
Collect approximately 400 additional annotations
Improve class balance
Evaluate on unseen field images
Continue documenting model performance


