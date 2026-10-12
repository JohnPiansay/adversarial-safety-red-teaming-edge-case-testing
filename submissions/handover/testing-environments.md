# Verified Testing Environments

This record covers local workbench verification only; no AI target environment has been tested.

## Local workbench

| Environment | Version/configuration | Verification date | Result |
|---|---|---|---|
| Windows local project | Python 3.15.0 via `py`; standard-library-only project | 2026-10-12 | All five unit tests passed; `workbench.py status` completed and reported six submission spaces and eleven files. |

## Execution summary

From the project directory, run `py -m unittest -v` to execute the workbench unit tests. Run `py workbench.py status` to inspect the submission layout. The captured local test evidence is in `submissions/execution-evidence/workbench-tests.md`.

This verification covers the Python workbench only. No AI target environment or target-system prompt-injection run has been verified.
