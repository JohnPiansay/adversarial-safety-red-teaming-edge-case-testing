# Adversarial Safety Red-Teaming & Edge Case Testing

A small, dependency-free Python workbench for organizing authorized safety-evaluation deliverables. It creates a dedicated submission directory for source files, test cases, run evidence, findings, release notes, and handover information.

## Quick start

```text
python workbench.py init
python workbench.py status
python -m unittest -v
```

Use `--root PATH` to create or inspect the submission layout in a different project directory. Initialization is safe to repeat: existing files are never overwritten.

## Submission spaces

- `submissions/source-files/` — requested code files submitted directly.
- `submissions/test-cases/` — test cases and the starter prompt-injection probes.
- `submissions/execution-evidence/` — run logs, outputs, and reproducibility evidence.
- `submissions/evaluation-summary-findings/` — evaluation summary and findings report.
- `submissions/submission-overview-release-notes/` — overview, release notes, and handover notes.
- `submissions/handover/` — verified environments and execution summary.

The starter probes are intentionally limited to instruction hierarchy, untrusted quoted content, persona overrides, and simulated tool-output injection. Run them only against systems you are authorized to evaluate. Record actual observations in execution evidence; do not treat expected behavior in a test case as a verified result.

## Publishing

This local scaffold is not yet a public GitHub repository. To publish it, create a public repository using the project title (or a GitHub-compatible slug such as `adversarial-safety-red-teaming-edge-case-testing`), then add the repository remote and push this project.
