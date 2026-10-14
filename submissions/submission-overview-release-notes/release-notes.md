# Submission Overview and Release Notes

This release separates verified local workbench checks from the submitter-reported Playground probe results.

## Deliverables

- Dependency-free Python command-line workbench for initializing and inspecting submission spaces.
- Four starter prompt-injection probes and unit tests for initialization, idempotency, preservation, and status reporting.
- Evaluation methodology, evidence records, release notes, and environment handover.

## Changes in this release

Updated probe evidence and findings to record four submitter-reported Playground runs with explicit scope and verification limitations. Refreshed local workbench verification: all five unit tests passed, and the status command reported six submission spaces and 12 files under Windows/Python 3.15.0.

## Handover

Run `py -m unittest -v` and `py workbench.py status` from the repository directory. See `VERIFICATION.md` and `submissions/execution-evidence/workbench-tests.md` for workbench evidence, and `submissions/execution-evidence/openai-playground-probes.md` for the reported target evaluation.

## Known limitations

The submitter reports all four starter probes met their narrow expected behaviors. Raw Playground logs or screenshots were not supplied for independent verification; the displayed model identity, run timestamps, settings-per-run, and fresh-session status remain unverified. PI-004 used simulated text in a user prompt, not a real tool-output channel. The four cases do not establish comprehensive guardrail resilience. Personal time records must be supplied by the account holder and are not verified by this project report.
