# YOLO Model Evaluation

This folder contains representative training and evaluation results from the latest YOLO model run for the **AI-Assisted Utility Asset Detection** project.

The model was developed to identify transportation and utility infrastructure assets from field imagery. The results provided here document model training, classification performance, and representative validation predictions.

## Contents

### Model Performance

* `results.png` — Training and validation metrics recorded during model training.
* `confusion_matrix.png` — Confusion matrix showing predicted versus actual asset classes.
* `confusion_matrix_normalized.png` — Normalized confusion matrix showing class-level performance.
* `BoxP_curve.png` — Precision curve for object detection.
* `BoxR_curve.png` — Recall curve for object detection.
* `BoxF1_curve.png` — F1 score curve for object detection.

### Validation Examples

The `validation_examples` folder contains representative validation images showing:

* Ground-truth labels
* Model predictions
* Detection performance on validation imagery

These examples provide a visual comparison between the annotated assets and the assets detected by the model.

## Interpreting the Results

The evaluation results illustrate overall model performance as well as differences in performance between individual asset classes. The confusion matrices and performance curves are particularly useful for identifying classes that are well detected and classes that may require additional training data or refinement.

The model is intended as an **engineering-assistance and field-identification tool**. Detection results should be reviewed and verified by an appropriately qualified engineer or field professional and should not be treated as a substitute for engineering judgment or field verification.

## Project Context

This model is one component of a broader **Caltrans Utility AI Assistant** concept that combines computer vision, retrieval-augmented engineering knowledge, project context, and engineering workflows.

Future development may connect detected assets directly with the engineering knowledge base so that an identified asset can be used to retrieve relevant requirements, procedures, and supplemental engineering guidance.

