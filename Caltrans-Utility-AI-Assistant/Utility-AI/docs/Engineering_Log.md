# Engineering Log

This log records specific engineering observations and decisions made during development of the AI-Assisted Utility Asset Detection project.

---

## Decision 001 — Telecommunications Pedestals

### Decision

Use a single `Telecom_Pedestal` class for Version 1 rather than attempting to distinguish telecommunications pedestal ownership.

### Observation

AT&T and Cox telecommunications pedestals exhibit significant visual overlap. Even experienced field engineers may require additional context to identify ownership reliably from imagery alone.

### Reasoning

A unified class provides a stronger training dataset while avoiding a classification distinction that cannot be reliably supported by visual evidence.

The class can be subdivided in a future version if sufficient examples and reliable distinguishing characteristics are identified.

---

## Decision 002 — Context Utilization

### Observation

Utility assets are often installed in characteristic groupings. For example, fire hydrants commonly have nearby isolation valves.

### Decision

The object detector will identify visible assets only. Engineering associations between assets will be handled by a separate knowledge layer rather than inferred directly by the visual detector.

### Reasoning

This separates **visual evidence** from **engineering reasoning**.

The detector answers:

> What visible assets are present?

The engineering knowledge layer can then consider:

> What engineering relationships, requirements, or next steps may be relevant?

This separation helps prevent the system from presenting an engineering inference as though it were directly observed in the image.

---

## Ongoing Log

Additional engineering decisions may be added as the project develops, particularly where field testing, model failures, or engineering requirements lead to changes in the computer vision workflow.
