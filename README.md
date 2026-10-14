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
- `submissions/execution-evidence/` — reproducible workbench test evidence and authorized target-system run evidence.
- `submissions/evaluation-summary-findings/` — methodology, evaluation status, results, and findings.
- `submissions/submission-overview-release-notes/` — deliverable overview, release notes, and limitations.
- `submissions/handover/` — verified local environment and execution summary.

## Verification status

The workbench has five unit tests recorded as passing under Python 3.15.0; the recorded status check reports all six submission spaces and eleven files. See [VERIFICATION.md](VERIFICATION.md) and `submissions/execution-evidence/workbench-tests.md` for that evidence.

The submitter reports personally running the four starter probes against the OpenAI Platform Playground and reports that all four met their narrow expected behaviors. The supplied response transcripts and evaluation limits are in `submissions/execution-evidence/openai-playground-probes.md` and `submissions/evaluation-summary-findings/evaluation-summary.md`. Raw Playground logs were not supplied for independent verification; the displayed model label, per-run settings, timestamps, and session isolation are therefore reported but not authenticated. These four cases are limited observations, not a general safety result.

## Safety and evidence

Run probes only against systems you are authorized to evaluate. Record the target, configuration, exact prompt, complete response, outcome, and evidence reference for each run. Treat expected behavior as a test criterion, not as proof of a pass. Do not record secrets or personal data in the reports. Distinguish your own actions from assistant-executed or AI-assisted work, and follow applicable disclosure requirements.

The public repository is [JohnPiansay/adversarial-safety-red-teaming-edge-case-testing](https://github.com/JohnPiansay/adversarial-safety-red-teaming-edge-case-testing).# Adversarial Safety Red-Teaming & Edge Case Testing

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
- `submissions/execution-evidence/` — reproducible workbench test evidence and, later, authorized target-system run evidence.
- `submissions/evaluation-summary-findings/` — methodology, evaluation status, results, and findings.
- `submissions/submission-overview-release-notes/` — deliverable overview, release notes, and limitations.
- `submissions/handover/` — verified local environment and execution summary.

## Verification status

The workbench has been tested locally: all five unit tests pass under Python 3.15.0, and the `status` command reports all six submission spaces and eleven files. See [VERIFICATION.md](VERIFICATION.md) and `submissions/execution-evidence/workbench-tests.md` for recorded evidence.

The starter probes have **not** been run against a target AI system. The evaluation report describes the methodology and records that target-system testing is pending; it does not claim a measured resilience result.

## Safety and evidence

Run probes only against systems you are authorized to evaluate. Record the target, configuration, exact prompt, complete response, outcome, and evidence reference for each run. Treat expected behavior as a test criterion, not as proof of a pass. Do not record secrets or personal data in the reports.

The public repository is [JohnPiansay/adversarial-safety-red-teaming-edge-case-testing](https://github.com/JohnPiansay/adversarial-safety-red-teaming-edge-case-testing).
