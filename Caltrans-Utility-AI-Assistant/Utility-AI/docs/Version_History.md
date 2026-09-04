# Version History

This document summarizes the evolution of the AI-Assisted Utility Asset Detection project. Each version represents an iterative engineering improvement informed by dataset quality, model evaluation, and real-world field testing.

---

## Version Summary

| Version | Primary Focus                         | Major Achievement                                                                   |
| ------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| V1.0    | Proof of Concept                      | Built the complete end-to-end workflow                                              |
| V2.0    | Dataset Refinement                    | Reduced classes from 34 to 21 and expanded the dataset                              |
| V2.1    | Evaluation Refinement                 | Improved evaluation methodology and transfer learning                               |
| V3.0    | Annotation Quality & Failure Analysis | Corrected annotations and introduced targeted dataset improvements                  |
| V4.0    | Dataset Expansion & Robustness        | Expanded the dataset, added difficult examples, and strengthened the evaluation set |

---

# Version 1.0 — Proof of Concept

**Released:** July 2026

## Objective

Establish a complete end-to-end computer vision workflow for detecting utility infrastructure from field imagery.

## Dataset

* 270 field images
* 772 annotated utility assets
* 34 object classes

## Major Achievements

* Built the first custom annotated dataset.
* Completed the full workflow from image collection through model evaluation.
* Successfully trained the first YOLO11 detection model.
* Established baseline performance for future comparison.

## Key Findings

Version 1 demonstrated that a working pipeline could successfully detect multiple utility asset types while highlighting several opportunities for improvement.

## Lessons Learned

* Dataset quality had a greater impact than model size.
* Rare classes reduced overall detection performance.
* Annotation consistency significantly affected results.
* Class taxonomy required simplification.

## Next Development Goals

* Consolidate object taxonomy.
* Improve class balance.
* Expand field imagery.
* Increase annotation consistency.

---

# Version 2.0 — Dataset Refinement

**Released:** August 2026

## Objective

Improve model performance through better data quality and class design.

## Major Improvements

* Reduced object taxonomy from 34 to 21 classes.
* Expanded the field image dataset.
* Improved annotation consistency.
* Increased representation of underrepresented utility assets.
* Applied transfer learning.

## Results

Version 2 produced a more balanced dataset and improved detection consistency across the primary utility classes.

This version also introduced expanded testing on unseen imagery to better understand real-world performance.

## Lessons Learned

* Better annotations produced measurable improvements.
* Transfer learning accelerated convergence.
* Validation metrics alone were not sufficient for evaluating practical performance.

---

# Version 2.1 — Evaluation Refinement

**Released:** August 2026

## Objective

Improve confidence in model evaluation and better understand the relationship between validation metrics and real-world performance.

## Major Improvements

* Rebalanced training and validation datasets.
* Compared multiple transfer learning strategies.
* Evaluated frozen-layer training.
* Improved model comparison methodology.

## Results

Version 2.1 demonstrated that changes in validation metrics did not always correspond to improved real-world detection performance.

This finding motivated a stronger emphasis on independent field testing and systematic failure analysis.

---

# Version 3.0 — Annotation Quality & Failure Analysis

**Development phase:** 2026

## Objective

Improve annotation quality and guide dataset development through systematic model failure analysis.

## Major Improvements

* Reviewed and corrected annotation inconsistencies.
* Tightened bounding boxes.
* Added difficult examples identified during testing.
* Added negative (background) images.
* Expanded the independent field test set.
* Continued transfer learning from the best Version 2 model.

## Current Findings

Version 3 reinforced the importance of evaluating models on independent field imagery rather than relying solely on validation metrics.

Areas requiring continued improvement included:

* Small utility assets
* Low-contrast pavement lids
* Partially occluded infrastructure
* Visually similar background objects

## Current Direction

Dataset expansion increasingly became driven by systematic failure analysis rather than random image collection.

---

# Version 4.0 — Dataset Expansion & Robustness

## Objective

Develop a larger, more representative dataset while improving robustness to difficult field conditions.

## Dataset

The Version 4 dataset contains:

* 804 images
* 804 corresponding label files
* 3,348 annotated utility assets
* 21 active object classes

## Major Improvements

* Expanded the dataset substantially from earlier versions.
* Continued correction of annotation inconsistencies.
* Tightened bounding boxes where appropriate.
* Added difficult field examples.
* Added background/negative images to improve false-positive handling.
* Developed a dedicated hard-test set for challenging examples.
* Continued iterative model training and evaluation.

## Engineering Approach

Version 4 continued the project's shift toward **failure-driven dataset development**.

Rather than treating additional images as automatically beneficial, new examples were selected to address specific weaknesses identified during model evaluation.

Particular attention was given to:

* Small or partially visible assets
* Low-contrast objects
* Occluded infrastructure
* Visually similar objects
* Difficult pavement and roadside environments
* False-positive conditions

## Current Direction

The project is continuing toward a more robust engineering-oriented computer vision system capable of supporting infrastructure inspection and utility asset identification workflows.

Future development areas include:

* Targeted dataset expansion
* Hard-test benchmark development
* Model robustness evaluation
* Mobile or edge inference
* GIS integration
* Integration with engineering knowledge systems and RAG
* AI-assisted engineering workflows

---

# Development Philosophy

The project follows an iterative engineering development cycle:

**Collect → Annotate → Train → Evaluate → Analyze Failures → Improve Dataset → Retrain**

The objective is not simply to achieve higher validation metrics, but to develop a model that performs reliably on the types of difficult imagery encountered in practical engineering environments.

This approach has made **dataset quality, independent testing, and failure analysis** central to the continued development of the system.

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
