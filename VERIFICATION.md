# Deliverables Verification Record

Verification date: 2026-10-12  
Local environment: Windows; Python 3.15.0 via the `py` launcher.

## Checklist

| Acceptance item | Status | Evidence and boundary |
|---|---|---|
| Deliverables tested and verified locally | Verified for the workbench | `py -m unittest -v`: 5 tests passed. `py workbench.py status`: completed successfully; six submission spaces and eleven files reported. This does not test an AI target. |
| Prompt instructions and acceptance criteria satisfied | Partially verified | The workbench and deliverable layout are implemented and tested. The four adversarial probes have not been run against a specified target, so end-to-end guardrail evaluation is outstanding. |
| No placeholder or dummy code in submitted files | Verified for executable code; report documents state their real status | `workbench.py` and its tests are functional. Report documents have substantive methodology/status instead of empty sections. “Not run” in the evaluation report is a factual status, not a claimed result. Recheck documents after editing before submission. |
| Time logged accurately reflects verified active work | Not independently verifiable here | No personal task-platform timer or time log was accessed. The account holder must enter only their own accurately recorded active work; no duration is asserted in this record. |

## Reproduction

Run from this project directory:

```powershell
py --version
py -m unittest -v
py workbench.py status
```

## Test results

Python reported version 3.15.0. All five tests passed:

- `test_initialize_creates_each_space_and_starter_artifacts`
- `test_initialize_is_idempotent_and_preserves_existing_files`
- `test_inspect_handles_uninitialized_root`
- `test_inspect_reports_spaces_and_file_counts`
- `test_submission_documents_are_populated`

The status command reported one file in `source-files`, two in `test-cases`, two in `execution-evidence`, two in `evaluation-summary-findings`, two in `submission-overview-release-notes`, and two in `handover` (eleven files total).

## Remaining evidence needed

To verify target-system acceptance, identify an authorized target and configuration, run each starter probe, and preserve the exact prompts and complete responses in `submissions/execution-evidence/`. Update the evaluation report only from those observations. Timekeeping must be verified from the user's own contemporaneous records.
