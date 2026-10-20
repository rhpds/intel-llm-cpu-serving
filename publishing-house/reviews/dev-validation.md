# Dev validation evidence

## Development validation — 2026-10-20

Dallas OCP 4.18.16 is a dev environment, separate from the proposed published target. Tests did not order a catalog item or establish published-lab acceptance. Existing dev model credentials were used only in memory for short synthetic requests; they were not copied into fixture workloads.

- Real completion with `granite-2b-cpu`: PASS.
- Old AnythingLLM image failed under the restricted OpenShift UID. Pinned workbench image, correct working directory and PVC mount: startup/HTTPS 200 PASS without SCC changes.
- Full RAG document ingestion, embeddings and answer grounding remain pending. API completion and UI startup do not establish that path.

Source fixes and this migration draft need author/reviewer acceptance. No workstream is marked complete.
