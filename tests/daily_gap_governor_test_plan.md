# APEX Daily Gap Governor Test Plan v0.1

Status: SPECIFIED / NOT YET RUN

Purpose: verify that the Daily Gap Governor can create a minimal evidence receipt without inflating truth status.

Test 1: active gap registry exists.
Pass condition: gaps/active_gaps.json is present and contains GAP-OCODE-RUNTIME-001.

Test 2: receipt generation path exists.
Pass condition: daily_receipts/ contains a receipt file after each run.

Test 3: confidence ledger exists.
Pass condition: confidence/gap_confidence_ledger.json records confidence before and after.

Test 4: no unsupported promotion.
Pass condition: truth status does not move to TESTED_IN_SCOPE unless a real test result exists.

Test 5: next smallest action exists.
Pass condition: decisions/latest_next_smallest_action.md names one bounded next step.

Hard stop: fail the run if evidence is missing, truth is inflated, or scale state is unlocked.
