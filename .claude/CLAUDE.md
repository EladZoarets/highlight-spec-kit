# CLAUDE.md

## Scope
This repository implements Track 1 (Spec Kit) of the assignment.

Do not implement BMAD here.
Do not introduce agents, subagents, or orchestration.

## Source of Truth
Always follow these files:

1. docs/assignment.md
2. docs/spec.md
3. docs/design.md

If code conflicts with the spec or design, follow the spec/design.

## Implementation Rules
- Use plain Python.
- Prefer simple functions.
- No external libraries.
- No API, database, UI, or network calls.
- Logic only.

## Input
Read input from:
data/sample_input.json

## Output
The program must:
- score events using deterministic rules
- ignore events with score = 0
- sort events by score (descending)
- return highlights with a score and short reason

## Error Handling
- Missing fields should not break the program.
- Raise ValueError only when the preference object is empty.

## Coding Style
- Keep code simple and readable.
- Avoid unnecessary architecture.
- Keep the solution small and demo-friendly.