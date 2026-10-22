# CPU Serving: learner validation and PH author review

Tracking: [GPTEINFRA-17783](https://issues.redhat.com/browse/GPTEINFRA-17783); [RHDPCD-2140](https://issues.redhat.com/browse/RHDPCD-2140).

## Reviewable fixes

Corrected the RAG exercise to capture the returned workspace slug and every uploaded document location, verify workspace membership after embedding, and require the fictional Northstar policy fact plus its citation. The synthetic document replaces an uncontrolled public-policy page and makes the grounding test observable. API entry is hidden from shell history. A missing-evidence question and repeated answer remain explicit human checks.

## Verification boundary

19 local regression tests pass (including eight author-workspace auth checks). Antora 3.1.14 builds the current learner source. These are offline author-package results; synthetic service replies do not establish real model or catalog acceptance.

Fresh Dallas granite-2b-cpu completion passed on October 22. Full workbench upload, native embedding, grounded answer, UI and missing-evidence behavior remain unqualified. Oberon is a proposed alternate development model service; its saved session is expired and no live Oberon capability is claimed.

## Requested reviewer actions

Approve the workbench/embedding image and platform, allocate the model connection, replay Modules 4–6 including repeated source inspection and missing-evidence handling, then perform the independent timed pilot, tenant isolation, key lifecycle and capacity checks.

PH maintainers must accept the intake/design, run supported RCARS/intake ingestion and generate the AgnosticV/QA wiring. Browser PH notes are the available reconciliation channel; local API access is unavailable. Dallas and Oberon are development environments, not catalog-onboarding substitutes. Do not advance acceptance tasks or PH stages from these offline checks. Preserve the related source/reference PR history and keep every RHDP PR linked to its onboarding Jira.

API response shapes were checked against the upstream [document API](https://github.com/Mintplex-Labs/anything-llm/blob/master/server/endpoints/api/document/index.js) and [workspace API](https://github.com/Mintplex-Labs/anything-llm/blob/master/server/endpoints/api/workspace/index.js). In particular, update-embeddings returns a workspace rather than a success flag. Live compatibility with the pinned workbench image remains part of the replay gate.
