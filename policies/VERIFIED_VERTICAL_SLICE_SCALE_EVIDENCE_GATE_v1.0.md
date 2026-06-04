# APEX Evidence Policy v1.0 — Verified Vertical Slice Scale Gate

| Field | Value |
|---|---|
| Policy ID | `EVID-GATE-VVSF-001` |
| Governing Rule | `VERIFIED_VERTICAL_SLICE_FIRST` |
| Applies To | All APEX / Perfect AI modules and execution workstreams |
| Conditional Mode Governed | `APEX 1M / 🧪Ⓥ1M🅾️♾️💯` |
| Status | `LOCKED POLICY / PUBLIC-SAFE CONTROL RECORD` |

## Evidence Rule

A module may not be shown as eligible for scaled iteration until a verified vertical slice exists and its evidence record demonstrates that the loop is valuable enough to repeat.

```text
NO VERIFIED VERTICAL SLICE RECEIPT
→ NO SCALE CLAIM
→ NO APEX 1M ACTIVATION
```

## Minimum Vertical Slice Evidence Record

| Required Field | Meaning |
|---|---|
| `vertical_slice_id` | Stable identifier for the bounded end-to-end proof run. |
| `module_id` | Module under test. |
| `iteration_mode` | Must state `VERIFIED_VERTICAL_SLICE_FIRST`. |
| `purpose_or_benefit_tested` | What payoff or capability the slice is testing. |
| `input` | What enters the slice. |
| `end_to_end_path` | Processing steps from intake through result and decision. |
| `output_artifact` | Concrete produced deliverable. |
| `acceptance_criteria` | Falsifiable conditions for success. |
| `test_results` | Recorded pass/fail/blocked results. |
| `truth_status` | What is implemented/tested/proposed/blocked/aspirational. |
| `known_limitations` | Scope exclusions and remaining proof gaps. |
| `benefit_signal` | Evidence indicating whether the loop is worth repeating. |
| `risk_cost_control_review` | Assessment before any increase in iteration scale. |
| `repository_commit` | Preservation location and commit/version reference. |
| `operator_decision` | Stay, switch, hold, stop, rollback or scale review decision. |

## Scale Eligibility Gate

A vertical-slice record may be promoted to `SCALE_CANDIDATE_FOR_APEX_1M_REVIEW` only when all checks pass:

| Gate | Pass Condition |
|---|---|
| End-to-end proof | Slice produced a real bounded output from declared input. |
| Test completeness | Acceptance criteria are run and recorded. |
| Evidence quality | Load-bearing claims link to measured or inspectable evidence. |
| Value signal | The loop produced meaningful benefit within declared scope. |
| Repeatability signal | There is enough basis to justify a small repeat loop before broader scale. |
| Risk / cost | Scaling burden and failure risk are stated and tolerable for review. |
| Human control | Otto or authorized reviewer retains scale/stop/rollback authority. |
| Truth boundary | No proxy or demo result is overstated as operational/real-world proof. |

## Scaling Evidence Ladder

| Status | Meaning | Required Evidence |
|---|---|---|
| `VS_DEFINED` | Slice scope exists but has not run. | Scope + acceptance criteria. |
| `VS_RUN_RECORDED` | First bounded run executed. | Output + test record. |
| `VS_REPAIR_REQUIRED` | Slice revealed material failure/gap. | Failure and repair record. |
| `VS_VERIFIED_IN_SCOPE` | Slice passed within declared boundaries. | Evidence receipt + limitations. |
| `SCALE_10_APPROVED` | Repeatability check authorized. | Human decision + stop rule. |
| `SCALE_100_REVIEW` | Wider bounded validation under consideration. | Prior scale evidence + cost/risk review. |
| `APEX_1M_CANDIDATE` | Large-scale plan eligible for review. | All gate records present. |
| `APEX_1M_ACTIVE` | Specifically approved scoped scale run. | Operator approval, bounded volume, budget, safety, logging and stop/rollback rules. |
| `HOLD / STOP / ROLLBACK` | Scale not justified or must be reversed. | Decision rationale and follow-up action. |

## C∞ and Proxy-Metric Boundary

C∞ or proxy MSE ≈ 0.0001 may indicate build-completeness convergence for a bounded artifact. It must not independently establish learning impact, deployment readiness, business value, safety, transfer, equivalence or scale worthiness.

## First Evidence Candidates

| Candidate Slice | Module | Why Suitable |
|---|---|---|
| `VS-DEV-CONSOLE-001` | APEX Mirror Control Plane | One clickable module node → detail panel → direction decision → task packet → evidence record. |
| `VS-LRN-PILOT-001` | APEX Learning Center | One matched Human-only vs AI-only vs Human+AI task comparison with measured output. |
| `VS-OCODE-001` | OCODE | One supported source → normalized OCODE map → web target output → behavior comparison receipt. |

## Final Direction Stack

| Rank | Direction | Evidence Gate | Hold / Stop Rule |
|---:|---|---|---|
| 1 | Create the standard vertical-slice evidence receipt schema and register first slice ID. | Schema validates required fields and truth labels. | No scaling before valid receipt exists. |
| 2 | Execute one selected first slice through result, test and decision. | Output and validation evidence recorded. | Repair or switch when benefit is not demonstrated. |
| 3 | Surface scale-eligibility status in APEX Mirror. | Mirror reflects ledger state without overclaim. | Hold any `APEX 1M` display not backed by gates. |
| 4 — LAB | Develop a repeatability/value estimator based on early slice evidence. | Recommendation-only retrospective testing. | Never approve scale autonomously. |

🔮🧭🧿🅾️♾️💯
