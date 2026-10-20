# Serve LLMs on Intel Xeon CPUs

## Delivery ownership

Migrate the existing Serve LLMs on Intel Xeon CPUs guided lab into Publishing House. Learners consume a platform-managed model endpoint and tenant key, connect a RAG frontend, load documents and evaluate responses. Standalone CPU model serving remains in rhpds/llm-cpu-serving. PH owns generated AgnosticV and RHDP onboarding; Dallas is the development test environment. Preserve source PR history. Tracking: GPTEINFRA-17783 and INTEL-46.

PH owns intake, reviews, Env Setup, generated AgnosticV and onboarding. Existing catalog PRs are historical proposals for reference; they are not a parallel onboarding route. Dallas OCP 4.18.16 is a development test environment. The proposed published target is OCP 4.22, subject to PH infrastructure acceptance.

## Learner path

1. CPU Inference Fundamentals (15 min).
2. Explore Model-as-a-Service (15 min).
3. Query the Model API (15 min).
4. Wire a RAG Frontend (15 min).
5. Load and Chunk Documents (15 min).
6. Query with RAG (15 min).
7. Understand CPU Inference Performance (10 min).
8. Conclusion (5 min).

## Infrastructure and credential boundary

One assigned tenant namespace and tenant-scoped model access. No learner GPU or local model server is provisioned in the guided profile. Max 25 concurrent learners is a capacity proposal requiring validation, not a tested result. Preserve namespace isolation, short-lived key creation/revocation and workload-owned cleanup.

## Acceptance and evidence

Validate deployed images and terminal dependencies, then real model access and the full learner workflow. Record source/image revisions, failure behavior, tenant isolation and cleanup. CPU placement requires serving-team evidence. Remaining RCARS overlap review, model allocation, capacity and author acceptance are explicit intake gates.

Tracking: RHDPCD-2140; GPTEINFRA-17783 / INTEL-46.
