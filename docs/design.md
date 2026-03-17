# Design: AI Highlight Selector

## Design Goal
Implement a minimal and deterministic highlight selector based on user preference and event scoring.

## Architecture
The solution contains four logical steps:

1. Input Parsing
2. Event Scoring
3. Sorting and Selection
4. Explanation Generation

## System Flow
Input JSON
→ score each event
→ discard score = 0
→ sort by score descending
→ generate explanation
→ return selected highlights

## Main Functions

### score_event(event, preference)
Calculates the score for a single event based on:
- favorite player match
- favorite team match
- event type

Returns:
- numeric score
- applied rules

### generate_reason(applied_rules)
Creates a short plain-English explanation for why the event was selected.

Returns:
- reason string

### select_highlights(events, preference)
Processes all events, filters irrelevant ones, sorts the results, and returns the selected highlights.

Returns:
- list of highlights with event, score, and reason

## Scoring Logic
Deterministic additive scoring:

- favorite player match = +8
- favorite team match = +5
- goal = +4
- assist = +3
- card = +1

## Sorting and Tie-Breaking
Events are sorted by:
1. score descending
2. event type priority
3. earlier minute

Event type priority:
- goal
- assist
- card

## Error Handling
- missing player or team fields do not cause failure
- empty events list returns an empty list
- empty preference falls back to event-type scoring only

## Demo Plan
Use `data/sample_input.json` as input.
Run the script with:

`python3 src/highlight_selector.py`

Validate that:
- scores match the scoring rules
- output is sorted correctly
- each selected highlight includes a reason
