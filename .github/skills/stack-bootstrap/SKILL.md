---
name: stack-bootstrap
description: Bootstrap the smallest VenturaGenArt Python structure for the approved visual generation MVP using declared stack needs. Use when the repository is ready to move from incubation docs to executable code. Do not use when a functional pipeline already exists or the task is only product scoping.
---

# Stack bootstrap

- Confirm the approved visual workflow before adding dependencies.
- Pin only packages needed for the first documented model path.
- Separate application code tests prompts and small reference assets.
- Keep model weights caches and generated galleries out of Git.
- Add one deterministic or seed-controlled smoke test where the stack permits it.
- Document hardware model source and local run assumptions.
- Reuse the shared repository CI standard.
