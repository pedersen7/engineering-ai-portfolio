# Version History

This document summarizes the evolution of the AI-Assisted Utility Asset Detection project. Each version represents an iterative engineering improvement informed by dataset quality, model evaluation, and real-world field testing.

---

| Version | Primary Focus      | Major Achievement                                                           |
| ------- | ------------------ | --------------------------------------------------------------------------- |
| V1.0    | Proof of Concept   | Built the complete end-to-end workflow                                      |
| V2.0    | Dataset Refinement | Reduced classes from 34 to 21 and expanded the dataset                      |
| V2.1    | Evaluation         | Improved validation methodology and transfer learning                       |
| V3.0    | Failure Analysis   | Introduced independent field benchmarking and targeted dataset improvements |

---

# Version 1.0 — Proof of Concept

**Released:** July 2026

## Objective

Establish a complete end-to-end computer vision workflow for detecting utility infrastructure from field imagery.

## Dataset

- 270 field images
- 772 annotated utility assets
- 34 object classes

## Major Achievements

- Built the first custom annotated dataset.
- Completed the full workflow from image collection through model evaluation.
- Successfully trained the first YOLO11 detection model.
- Established baseline performance for future comparison.

## Key Findings

Version 1 demonstrated that a working pipeline could successfully detect multiple utility asset types while highlighting several opportunities for improvement.

## Lessons Learned

- Dataset quality had a greater impact than model size.
- Rare classes reduced overall detection performance.
- Annotation consistency significantly affected results.
- Class taxonomy required simplification.

## Next Development Goals

- Consolidate object taxonomy.
- Improve class balance.
- Expand field imagery.
- Increase annotation consistency.

---

# Version 2.0 — Dataset Refinement

**Released:** August 2026

## Objective

Improve model performance through better data quality and class design.

## Major Improvements

- Reduced object taxonomy from 34 to 21 classes.
- Expanded the field image dataset.
- Improved annotation consistency.
- Increased representation of underrepresented utility assets.
- Applied transfer learning.

## Results

Version 2 produced a more balanced dataset and improved detection consistency across the primary utility classes.

This version also introduced expanded testing on unseen imagery to better understand real-world performance.

## Lessons Learned

- Better annotations produced measurable improvements.
- Transfer learning accelerated convergence.
- Validation metrics alone were not sufficient for evaluating practical performance.

---

# Version 2.1 — Evaluation Refinement

**Released:** August 2026

## Objective

Improve confidence in model evaluation.

## Major Improvements

- Rebalanced training and validation datasets.
- Compared multiple transfer learning strategies.
- Evaluated frozen-layer training.
- Improved model comparison methodology.

## Results

Version 2.1 demonstrated that changes in validation metrics did not always correspond to improved real-world detection performance.

This finding motivated a stronger emphasis on independent field testing.

---

# Version 3.0 — Annotation Quality & Failure Analysis

**Released:** July 2026 (Initial Release)

## Objective

Improve annotation quality and guide dataset development through systematic model failure analysis.

## Major Improvements

- Reviewed and corrected annotation inconsistencies.
- Tightened bounding boxes.
- Added difficult examples identified during testing.
- Added negative (background) images.
- Expanded the independent field test set.
- Continued transfer learning from the best Version 2 model.

## Current Findings

Version 3 reinforced the importance of evaluating models on independent field imagery rather than relying solely on validation metrics.

Current areas for improvement include:

- Small utility assets
- Low-contrast pavement lids
- Partially occluded infrastructure
- Visually similar background objects

## Current Direction

Future dataset expansion is now driven by systematic failure analysis rather than random image collection.

---

# Future Versions

Future development will continue to focus on practical engineering applications, including:

- Targeted dataset expansion
- Hard test benchmark development
- Mobile inference
- GIS integration
- Retrieval-Augmented Generation (RAG)
- AI-assisted engineering workflows
