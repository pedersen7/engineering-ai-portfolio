# Engineering Decisions

# AI-Assisted Utility Asset Detection

This document summarizes the major engineering decisions made throughout the development of the Utility Asset Detection project. Rather than simply recording project progress, it explains the reasoning behind key technical choices and how each decision influenced subsequent development.

---

# Design Philosophy

The objective of this project is not simply to maximize benchmark accuracy, but to develop a practical computer vision workflow capable of supporting engineering tasks under real-world conditions.

Throughout development, engineering decisions have been guided by three principles:

- Improve dataset quality before increasing model complexity.
- Validate performance using real-world imagery.
- Use model failures to drive continuous improvement.

---

# Decision 1 — Develop a Custom Dataset

## Challenge

Public computer vision datasets contain very few examples of utility infrastructure commonly encountered during transportation and utility engineering projects.

## Decision

Develop a completely custom dataset using original field photographs collected throughout Southern California.

## Reasoning

A custom dataset allows:

- Engineering-specific object classes.
- Consistent annotation standards.
- Control over image quality.
- Progressive dataset expansion.
- Continuous refinement as new challenges are identified.

---

# Decision 2 — Simplify the Class Taxonomy

## Challenge

The original dataset contained 34 object classes, several of which contained very few examples or represented visually similar infrastructure.

## Decision

Reduce the dataset to a refined 21-class taxonomy.

## Reasoning

Simplifying the class structure:

- Increased the number of examples per class.
- Reduced ambiguity between similar objects.
- Improved annotation consistency.
- Better reflected practical engineering workflows.

The revised taxonomy also simplified future dataset maintenance.

---

# Decision 3 — Prioritize Annotation Quality

## Challenge

Early development identified inconsistencies in class assignment and bounding box placement.

## Decision

Review and improve existing annotations rather than simply collecting more images.

## Reasoning

Improving annotation quality was expected to provide greater long-term benefit than increasing dataset size alone.

Examples included:

- correcting class inconsistencies
- tightening bounding boxes
- removing accidental annotation errors
- improving consistency between similar infrastructure types

---

# Decision 4 — Use Transfer Learning

## Challenge

Training a detector from scratch requires significantly larger datasets.

## Decision

Continue development using transfer learning from previously trained models.

## Reasoning

Transfer learning:

- reduced training time
- accelerated convergence
- retained useful visual features learned during previous training
- allowed development to focus on dataset improvement rather than relearning basic object features

---

# Decision 5 — Introduce Independent Field Testing

## Challenge

Validation metrics alone do not always represent practical field performance.

## Decision

Evaluate models using an independent collection of unseen roadway images.

## Reasoning

These images include conditions commonly encountered during engineering field work, including:

- varying viewing angles
- partially occluded assets
- small utility infrastructure
- cluttered urban environments
- changing lighting conditions

Independent field testing provides additional confidence when comparing model versions.

---

# Decision 6 — Use Failure Analysis to Guide Data Collection

## Challenge

Randomly collecting additional photographs becomes increasingly inefficient as the dataset grows.

## Decision

Allow model failures to determine future data collection priorities.

## Reasoning

Instead of collecting images at random, new field photographs are selected to address observed weaknesses.

Examples include:

- missed water valve lids
- low-contrast pavement features
- gas lid confusion
- telecom versus electrical infrastructure
- transformers under varied conditions
- visually similar background objects

This targeted approach improves dataset diversity while reducing unnecessary duplication.

---

# Decision 7 — Include Negative Images

## Challenge

Infrastructure environments contain many objects that visually resemble utility assets.

## Decision

Include background images that intentionally contain similar non-target infrastructure.

## Reasoning

Negative images help reduce false positives by teaching the model what should not be detected.

Examples include:

- trolley and catenary infrastructure
- construction features
- roadway markings
- pavement repairs
- miscellaneous roadside objects

---

# Decision 8 — Focus on Practical Performance

Project success is evaluated using multiple criteria rather than a single benchmark score.

Current evaluation considers:

- annotation quality
- validation metrics
- independent field testing
- false positives
- false negatives
- engineering usefulness

This broader evaluation strategy reflects the practical requirements of engineering applications, where reliable performance under varied field conditions is often more important than achieving the highest validation score.

---

# Ongoing Engineering Approach

Development follows a continuous improvement cycle.

Field Collection

↓

Annotation

↓

Model Training

↓

Validation

↓

Independent Field Testing

↓

Failure Analysis

↓

Targeted Dataset Improvement

↓

Next Model Version

Rather than treating model development as a single training exercise, the project is approached as an iterative engineering process in which every model version informs the next.
