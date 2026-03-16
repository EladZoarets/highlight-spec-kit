# Generative AI Evangelist – Assignment

## Goal
Demonstrate a structured AI-assisted development process using both Spec Kit and BMAD methodologies.

The same feature must be developed using both approaches and then compared.

## Feature to Build
AI Highlight Selector

The system selects the most relevant highlights from a list of game events based on a user's preference.

## Input
1. List of game events (JSON)

Each event may include:
- event type
- player
- team
- minute

Example:
{
  "type": "goal",
  "player": "Messi",
  "team": "Inter Miami",
  "minute": 34
}

2. User preference

Supported preferences:
- favorite_player
- favorite_team

Example:
{
  "favorite_player": "Messi",
  "favorite_team": "Inter Miami"
}

## Output
A list of selected highlights.

Each highlight must include:
- the original event
- a numeric score
- a short explanation describing why it was selected

Example output:
[
  {
    "event": {...},
    "score": 10,
    "reason": "favorite player involved, goal event"
  }
]

## Constraints
- No video processing required
- Logic only
- Simple implementation is sufficient

## Required Tracks

### Track 1 – Spec Kit
Show the development process using a structured specification-first approach.

Steps:
1. Feature specification
2. System design
3. Implementation
4. Validation

### Track 2 – BMAD
Develop the same feature using an iterative AI-driven approach.

The process may include:
- exploration
- prompting
- iteration
- validation
- optional subagents

### Track 3 – Comparison
Provide a short comparison between Spec Kit and BMAD.

Address:
- where each method adds value
- where it introduces friction
- which scales better across teams
- which fits GenAI-heavy development better
- how both approaches could be combined in a real organization

## Final Deliverable
A short presentation including:

1. Feature overview
2. Spec Kit development process and demo
3. BMAD development process and demo
4. Comparison and recommendation