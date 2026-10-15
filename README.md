# Adversarial Safety Red-Teaming & Edge Case Testing

A dependency-free Python workbench for organizing authorized evaluations of LLM guardrail resilience.

## Quick start

From the repository root, run:

```powershell
py workbench.py init
py workbench.py status
py -m unittest -v
```

Use `--root PATH` with `init` or `status` to select another project directory. Initialization is safe to repeat and preserves files that already exist.

## Workbench spaces

- `submissions/source-files/` — requested source files.
- `submissions/test-cases/` — synthetic boundary and prompt-injection test cases.
- `submissions/execution-evidence/` — local test evidence and approved, sanitized evidence references.
- `submissions/evaluation-summary-findings/` — local evaluation notes and findings.
- `submissions/submission-overview-release-notes/` — local handover and release notes.
- `submissions/handover/` — environment and execution records.

Narrative reports, raw transcripts, and sensitive evidence should be kept outside this public repository. The `.gitignore` excludes designated local report artifacts; it does not remove files already tracked, so review repository contents before committing.

## Scope and safety

Run probes only against systems and personas you are authorized to evaluate. Record the target, configuration, expected behavior, complete observed response, outcome, and evidence reference for each test. Treat expected behavior as a criterion, not as proof of a pass. Do not store secrets or personal data in this repository. Distinguish observed results from interpretation and follow applicable school or organization disclosure requirements.
