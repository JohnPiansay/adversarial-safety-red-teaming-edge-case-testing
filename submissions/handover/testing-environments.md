# Verified Testing Environments

This handover separates the workbench checks run locally from the submitter-reported Playground evaluation.

## Local workbench

| Environment | Version/configuration | Verification date | Result |
|---|---|---|---|
| Windows local project | Python 3.15.0; standard-library-only project | 2026-10-13 | All five unit tests passed; `workbench.py status` reported six submission spaces and 12 files. See `submissions/execution-evidence/workbench-tests.md`. |

## Reported target evaluation

| Target | Configuration as reported | Evidence status |
|---|---|---|
| OpenAI Platform Playground, displayed model label `gpt-6-luna` | Standard tier; WebSocket on; text format; standard reasoning, medium effort; medium verbosity; automatic summary; Store logs enabled; no tools or system/developer prompt reported | Submitter reports four probes run and passing. Response transcripts are in `submissions/execution-evidence/openai-playground-probes.md`; raw logs and screenshots were not supplied for independent verification. Model identity, per-run settings, timestamps, and session isolation remain unverified. |

## Execution summary

From the project directory, run `py -m unittest -v` for the workbench tests and `py workbench.py status` to inspect the layout. These commands verify local workbench behavior only. The reported Playground probe results are separate and have the evidence limitations listed above.
