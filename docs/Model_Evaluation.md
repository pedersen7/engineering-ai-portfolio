# Model Evaluation

## Overview

The Utility Asset Detection project uses multiple evaluation methods to
measure model performance throughout development.

Rather than relying solely on validation metrics, each model is also
evaluated using independent field images that were never included in
training or validation.

This approach provides a more realistic assessment of how the model is
likely to perform in practical engineering applications.

---

## Evaluation Process

Training Dataset
        ↓
Validation Metrics
        ↓
Independent Field Testing
        ↓
Failure Analysis
        ↓
Dataset Improvements
        ↓
Next Model Version

---

## Standard Evaluation Metrics

Each model is evaluated using the metrics generated during YOLO training,
including:

- Precision
- Recall
- mAP50
- mAP50-95
- Confusion Matrix
- Precision-Recall Curves
- Validation Loss

These provide an objective comparison between model versions.

---

## Independent Field Testing

In addition to standard validation metrics, models are evaluated on a
separate collection of field photographs that are intentionally excluded
from the training dataset.

These images include:

- Different lighting
- Various viewing angles
- Vehicle-based photographs
- Small utility assets
- Partial occlusions
- Visually cluttered environments

This testing better represents real-world engineering conditions.

---

## Failure Analysis

Incorrect detections are reviewed manually.

Typical observations include:

- Missed detelectrical vaults in asphalt
- Confusion between telecom and electrical assets
- Small utility lids
- Low contrast objects
- False positives on pavement features

These observations guide future dataset improvements.

---

## Current Evaluation Strategy

Development is driven by an iterative engineering workflow.

Rather than simply increasing the number of training images,
additional data collection is targeted toward weaknesses identified
during model evaluation.

This continual feedback loop has become a core design principle of
the project.
