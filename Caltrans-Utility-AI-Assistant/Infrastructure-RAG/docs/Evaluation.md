# RAG System Evaluation

## Overview

The Infrastructure Engineering RAG Assistant was evaluated using a structured set of engineering questions designed to test retrieval quality, reranking performance, source identification, and response usefulness.

The evaluation process was developed to answer a practical engineering question:

> Can the RAG system consistently identify and prioritize the engineering information most relevant to a user's question?

The evaluation also helped identify situations where retrieval was technically related to the question but not sufficiently precise for engineering decision support.

---

## Evaluation Dataset

The evaluation set contains:

* **63 engineering questions**
* Questions covering utility engineering, encroachments, permits, installation requirements, definitions, and related engineering topics
* Expected-page references for questions where a reliable page-level reference could be established
* Diagnostic review of retrieved documents and page rankings

Of the 63 questions, **22 had usable expected-page references** suitable for page-level retrieval evaluation.

The remaining questions were still useful for qualitative evaluation of retrieval and response behavior.

---

## Evaluation Approach

The evaluation was performed in stages.

### 1. Baseline Retrieval

The initial system used semantic vector retrieval against the Chroma vector database.

The evaluation examined whether relevant engineering documents and passages appeared among the retrieved results.

### 2. Expanded Candidate Retrieval

The retrieval stage was expanded to provide a larger candidate set before final ranking.

The system retrieves **20 candidate chunks** before reranking.

This provides the reranker with a broader set of potentially relevant material rather than relying solely on the initial vector ranking.

### 3. Cross-Encoder Reranking

A cross-encoder reranker was added to evaluate the relationship between the user's question and each retrieved candidate.

The implementation uses:

`cross-encoder/ms-marco-MiniLM-L-6-v2`

The purpose of reranking is to improve the ordering of retrieved material so that the most directly relevant engineering passages are prioritized.

---

## Evaluation Dimensions

The evaluation considered several aspects of system performance.

### Retrieval Relevance

Does the system retrieve material that actually addresses the question?

This is more demanding than simply determining whether a retrieved passage contains similar terminology.

### Page Identification

When an expected page reference is available, does the retrieval process identify the correct page or an appropriately relevant nearby passage?

### Reranking Performance

Does the cross-encoder improve the position of the most relevant material within the retrieved candidate set?

### Engineering Response Quality

Does the retrieved context provide sufficient information for the language model to produce a useful engineering response?

### Source Verification

Can the response be traced back to identifiable engineering source material?

### Ambiguity and Nuance

Some questions cannot be evaluated as simply correct or incorrect because multiple passages may provide valid context.

These cases require engineering judgment rather than a purely numerical retrieval score.

---

## Qualitative Review Categories

During evaluation, questions were reviewed using three practical categories:

| Category   | Meaning                                                                                                    |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| **Good**   | Retrieval and supporting context were sufficiently strong and directly relevant.                           |
| **Nuance** | Retrieval was useful, but interpretation, context, or engineering judgment was required.                   |
| **Verify** | The result required additional checking against the source material before being treated as authoritative. |

These categories were intentionally used alongside quantitative retrieval diagnostics rather than replacing them.

---

## Diagnostic Evaluation

The evaluation process also examined the retrieved pages and candidate rankings to identify failure modes.

Examples of retrieval behavior investigated included:

* The correct document was present but ranked too low.
* A semantically similar passage was retrieved instead of the most directly relevant passage.
* The correct engineering topic was identified but the supporting requirement was incomplete.
* Multiple related passages required contextual interpretation.
* The retrieval result appeared plausible but required source verification.
* The relevant information was distributed across more than one passage.

These diagnostics were useful for determining whether an apparent response problem originated from retrieval, ranking, available source material, or downstream language-model interpretation.

---

## Why Reranking Matters

Engineering questions often contain terminology that appears in multiple related sections of a technical document.

For example, a question may contain terms associated with:

* utility installation
* encroachment
* depth
* crossings
* permits
* materials
* construction requirements

A vector search system can identify passages that are semantically related without necessarily identifying the passage that most directly answers the question.

The cross-encoder provides a second-stage relevance assessment intended to improve this distinction.

The resulting architecture is therefore:

**Question → Vector Retrieval → Candidate Set → Cross-Encoder Reranking → Engineering Context → LLM Response**

---

## Evaluation Philosophy

The evaluation is intentionally focused on engineering usefulness rather than treating RAG as a generic question-answering benchmark.

A response can be linguistically convincing while still being unsuitable for engineering use if:

* the wrong requirement was retrieved;
* the source passage was incomplete;
* an exception was missed;
* a related but different requirement was used; or
* the supporting source cannot be verified.

For this reason, the evaluation emphasizes **retrieval quality, source traceability, and engineering judgment** in addition to response quality.

---

## Current Findings

The evaluation demonstrated the value of examining the retrieval pipeline independently from the final language-model response.

The 63-question evaluation set provided a practical test bed for comparing retrieval behavior, investigating difficult questions, and identifying opportunities for improvement.

The addition of cross-encoder reranking provides a more deliberate second-stage relevance assessment than relying exclusively on vector similarity.

The evaluation also showed that difficult engineering questions often require more than a simple "correct/incorrect" classification. Some results are best understood as useful retrieval that still requires engineering interpretation or verification.

---

## Limitations

The current evaluation should not be interpreted as a formal validation of engineering correctness.

Important limitations include:

* The evaluation dataset is relatively small.
* Only 22 questions currently have reliable page-level expected references.
* Some engineering questions have multiple potentially relevant source passages.
* Engineering interpretation may be required even when retrieval is successful.
* The evaluation uses a specific collection of engineering documents and may not generalize to other manuals or agencies.
* Final engineering decisions should continue to be verified against the applicable current source documents and standards.

---

## Future Evaluation

Future evaluation work may include:

* Expanding the evaluation question set.
* Increasing the number of questions with verified expected-page references.
* Measuring retrieval performance at different candidate-set sizes.
* Comparing vector-only retrieval against reranked retrieval.
* Tracking top-1, top-3, top-5, and top-20 retrieval performance.
* Measuring whether reranking consistently improves relevant-page position.
* Adding automated regression testing for previously evaluated questions.
* Evaluating additional engineering disciplines and document types.
* Tracking source-verification performance.
* Evaluating end-to-end engineering response quality.

---

## Relationship to the RAG Architecture

The evaluation process is an integral part of the Infrastructure RAG architecture.

The system is treated as a pipeline rather than a single AI model:

**Documents → Processing → Chunking → Embeddings → Retrieval → Reranking → Engineering Prompt → LLM → Verified Engineering Response**

Testing each stage helps identify where improvements are actually needed.

This approach supports a broader engineering principle:

> **Improve the information pipeline before assuming the language model is the problem.**

---

## Status

**Evaluation framework:** Active development

**Evaluation questions:** 63

**Questions with usable expected-page references:** 22

**Candidate retrieval before reranking:** 20

**Reranking:** Cross-Encoder

**Primary evaluation focus:** Retrieval relevance, page identification, reranking, source verification, and engineering response quality
