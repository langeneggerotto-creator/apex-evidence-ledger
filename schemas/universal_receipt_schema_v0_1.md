# APEX Universal Receipt Schema v0.1

Status: CANONICAL_CANDIDATE / DESIGNED_NOT_PROVEN

## Purpose
Unify evidence receipts, gap receipts, learning receipts, decision receipts, prediction receipts, simulation receipts, and build receipts under one Core OS object.

## Core definition
A receipt is a traceable state transition.

## Universal pattern
Prior state -> action or observation -> new state -> evidence -> confidence -> learning -> next decision.

## Required fields

receipt_id

receipt_type
Allowed values: EVIDENCE, GAP, LEARNING, DECISION, PREDICTION, SIMULATION, BUILD, GOVERNANCE, STATE_TRANSITION

created_utc

source_module

related_gap_id

objective

prior_state

action_or_observation

new_state

state_transition_claim

supporting_evidence

confidence_before

confidence_after

confidence_change

truth_status
Allowed values: OBSERVED, IMPLEMENTED, TESTED_IN_SCOPE, INFERRED, SIMULATED, DESIGNED_NOT_PROVEN, NEEDS_EVIDENCE, BLOCKED, NO_CHANGE_DETECTED

decision_impact

learning_extracted

next_smallest_action

human_review_needed

limitations

## Receipt quality gate
A receipt is useful only if it answers:

1. What changed?
2. What proves it changed?
3. Why does the change matter?
4. What decision changes next?
5. What remains unproven?

## Core law
Evidence becomes learning only when it changes future decisions.

## Truth boundary
This schema is specified but not yet validated against multiple real APEX module receipts.
