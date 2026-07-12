# Engineering Decisions

---

## Decision 001

### Telecommunications Pedestals

Decision:
Use a single Telecom_Pedestal class for Version 1. Group all telecommunications pedestals into a single class for Version 1.

Reason:
AT&T and Cox pedestals exhibit significant visual overlap. Even experienced field engineers often require additional context to identify ownership reliably. Grouping these assets creates a stronger training class while preserving the option to subdivide the class later if sufficient distinguishing evidence is collected.
Visual distinction between AT&T and Cox pedestals is often unreliable, even for experienced field engineers. A unified class produces a stronger training dataset while preserving the option to subdivide later if reliable distinguishing characteristics are identified.

---

## Decision 002

Context Utilization

Observation
Utility assets are often installed in characteristic groupings.
For example, fire hydrants commonly have nearby isolation valves.

Decision
The object detector will identify visible assets only.
Engineering associations between assets will be handled by the knowledge layer rather than inferred directly by the detector.

Reasoning
This separates visual evidence from engineering reasoning and allows recommendations without overstating certainty.

...

# Engineering Decisions

## Why YOLO11n?

...

## Why 34 Classes?

...

## Why Consolidate Classes for Version 2?

...

## Why Dataset Quality Was Prioritized Over Model Size?

...
