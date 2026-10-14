# Adversarial Safety Red-Teaming & Edge Case Testing

A dependency-free Python workbench and documentation set for organizing authorized guardrail-resilience evaluations. It creates dedicated submission spaces for source files, probes, execution evidence, findings, release notes, and handover information.

## Quick start

From this directory, run:

```powershell
py workbench.py init
py workbench.py status
py -m unittest -v
```

Use `--root PATH` with `init` or `status` to select another project directory. Initialization is safe to repeat and does not overwrite existing files.

## Submission spaces

- `submissions/source-files/` — requested source files.
- `submissions/test-cases/` — test cases and four starter prompt-injection probes.
- `submissions/execution-evidence/` — local workbench test evidence and reported target-system probe evidence.
- `submissions/evaluation-summary-findings/` — methodology, evaluation status, results, and findings.
- `submissions/submission-overview-release-notes/` — deliverable overview, release notes, and limitations.
- `submissions/handover/` — verified local environment and execution summary.

## Verification status

The latest checked snapshot of `main` passes all five workbench unit tests under Windows and Python 3.15.0. `py workbench.py status` reports six submission spaces and 12 files. Reproduction steps and results are in [VERIFICATION.md](VERIFICATION.md) and `submissions/execution-evidence/workbench-tests.md`.

The submitter reports personally running the four starter probes against the OpenAI Platform Playground and says the supplied responses met the probes' narrow expected behaviors. The transcripts and limitations are in `submissions/execution-evidence/openai-playground-probes.md` and `submissions/evaluation-summary-findings/evaluation-summary.md`. Raw Playground logs were not supplied for independent verification; the displayed model label, per-run settings, timestamps, and session isolation remain unauthenticated. These are four limited observations, not a general safety result.

## Safety and evidence

Run probes only against systems you are authorized to evaluate. Record the target, configuration, exact prompt, complete response, outcome, and evidence reference for each run. Treat expected behavior as a test criterion, not proof of a pass. Do not record secrets or personal data in the reports. Distinguish your own actions from assistant-executed or AI-assisted work, and follow applicable disclosure requirements.

The public repository is [JohnPiansay/adversarial-safety-red-teaming-edge-case-testing](https://github.com/JohnPiansay/adversarial-safety-red-teaming-edge-case-testing).
