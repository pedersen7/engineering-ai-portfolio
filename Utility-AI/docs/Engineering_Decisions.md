# Engineering Decisions

## AI-Assisted Utility Asset Detection

This document summarizes the major engineering decisions made throughout the development of the Utility Asset Detection project. Rather than simply recording project progress, it explains the reasoning behind key technical choices and how each decision influenced subsequent development.

---

## Design Philosophy

The objective of this project is not simply to maximize benchmark accuracy, but to develop a practical computer vision workflow capable of supporting engineering tasks under real-world conditions.

Throughout development, engineering decisions have been guided by three principles:

* Improve dataset quality before increasing model complexity.
* Validate performance using real-world imagery.
* Use model failures to drive continuous improvement.

---

## Decision 1 — Develop a Custom Dataset

### Challenge

Public computer vision datasets contain relatively few examples of utility infrastructure commonly encountered during transportation and utility engineering projects.

### Decision

Develop a custom dataset using original field photographs collected throughout Southern California.

### Reasoning

A custom dataset provides:

* Engineering-specific object classes.
* Consistent annotation standards.
* Control over image quality and content.
* Progressive dataset expansion.
* Continuous refinement as new challenges are identified.

---

## Decision 2 — Simplify the Class Taxonomy

### Challenge

The original dataset contained 34 object classes, several of which had very few examples or represented visually similar infrastructure.

### Decision

Reduce the dataset to a refined 21-class taxonomy.

### Reasoning

Simplifying the class structure:

* Increased the number of examples available for individual classes.
* Reduced ambiguity between similar objects.
* Improved annotation consistency.
* Better reflected practical engineering workflows.
* Simplified future dataset maintenance.

The revised taxonomy was intended to make the model more useful for practical infrastructure identification rather than attempting to distinguish every possible variation of an asset.

---

## Decision 3 — Prioritize Annotation Quality

### Challenge

Early development identified inconsistencies in class assignment and bounding-box placement.

### Decision

Review and improve existing annotations rather than simply collecting more images.

### Reasoning

Improving annotation quality was expected to provide greater long-term benefit than increasing dataset size alone.

Examples included:

* Correcting class inconsistencies.
* Tightening bounding boxes.
* Removing annotation errors.
* Improving consistency between similar infrastructure types.

This became an important part of the transition from early proof-of-concept datasets toward later model versions.

---

## Decision 4 — Use Transfer Learning

### Challenge

Training a detector from scratch generally requires substantially more data and computational resources.

### Decision

Use transfer learning from previously trained models as the project evolved.

### Reasoning

Transfer learning:

* Reduced training time.
* Accelerated convergence.
* Retained useful visual features learned during previous training.
* Allowed development effort to focus more heavily on dataset improvement and engineering-specific detection challenges.

---

## Decision 5 — Introduce Independent Field Testing

### Challenge

Validation metrics alone do not always represent practical field performance.

### Decision

Evaluate models using an independent collection of unseen roadway and field images.

### Reasoning

These images include conditions commonly encountered during engineering field work, including:

* Varying viewing angles.
* Partially occluded assets.
* Small utility infrastructure.
* Cluttered urban environments.
* Changing lighting conditions.

Independent field testing provides an additional perspective when comparing model versions and helps identify weaknesses that may not be apparent from standard validation metrics.

---

## Decision 6 — Use Failure Analysis to Guide Data Collection

### Challenge

Randomly collecting additional photographs becomes increasingly inefficient as the dataset grows.

### Decision

Allow observed model failures to determine future data-collection priorities.

### Reasoning

Instead of collecting images at random, new field photographs are selected to address observed weaknesses.

Examples include:

* Missed water valve lids.
* Low-contrast pavement features.
* Gas lid confusion.
* Telecom versus electrical infrastructure.
* Transformers under varied conditions.
* Visually similar background objects.

This targeted approach improves dataset diversity while reducing unnecessary duplication.

---

## Decision 7 — Include Negative Images

### Challenge

Infrastructure environments contain many objects that can visually resemble utility assets.

### Decision

Include background images that intentionally contain similar non-target infrastructure and other challenging visual features.

### Reasoning

Negative images help reduce false positives by providing examples of objects and environments that should not be detected as target classes.

Examples include:

* Trolley and catenary infrastructure.
* Construction features.
* Roadway markings.
* Pavement repairs.
* Miscellaneous roadside objects.

The use of negative examples reflects a broader shift toward evaluating not only what the model detects, but also what it incorrectly identifies.

---

## Decision 8 — Focus on Practical Performance

Project success is evaluated using multiple criteria rather than a single benchmark score.

Current evaluation considers:

* Annotation quality.
* Validation metrics.
* Independent field testing.
* False positives.
* False negatives.
* Engineering usefulness.

This broader evaluation strategy reflects the practical requirements of engineering applications, where reliable performance under varied field conditions can be more important than achieving the highest validation score.

---

## Ongoing Engineering Approach

Development follows a continuous improvement cycle:

**Field Collection → Annotation → Model Training → Validation → Independent Field Testing → Failure Analysis → Targeted Dataset Improvement → Next Model Version**

Rather than treating model development as a single training exercise, the project is approached as an iterative engineering process in which every model version informs the next.

The central principle is:

> **Model failures are engineering information.**

A missed asset, false positive, inconsistent annotation, or difficult field condition can identify a specific opportunity to improve the dataset, evaluation process, or detection workflow.

This approach has shifted the project from simply training a computer vision model toward developing a repeatable engineering-oriented AI development process.
