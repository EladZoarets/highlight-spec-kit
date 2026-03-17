# Spec: AI Highlight Selector

## 1. Overview

Selects the most relevant game highlights from a list of events based on a user preference, and returns a short explanation for each.

## 2. Goal

Score each game event against the user's preference (favorite player or team) and return the top matches with a reason.

## 3. Inputs

**Game events** — a JSON array. Each event has:
- `type` (string, required): `goal`, `assist`, or `card`
- `player` (string, optional)
- `team` (string, optional)
- `minute` (int, optional)

```json
[
  { "type": "goal", "player": "Messi", "team": "Inter Miami", "minute": 34 },
  { "type": "card", "player": "Ramos", "team": "Al Hilal", "minute": 67 }
]
```

**User preference** — a JSON object (all fields optional):
- `favorite_player` (string, optional)
- `favorite_team` (string, optional)

If at least one preference field is provided, matching events receive additional score based on the rules in Section 6.

If no preference fields are provided, scoring is based on event type only (no preference boost).

```json
{ "favorite_player": "Messi" }

## 4. Outputs

A JSON array sorted by score descending. Events with score 0 are excluded.

```json
[
  {
    "event": { "type": "goal", "player": "Messi", "team": "Inter Miami", "minute": 34 },
    "score": 12,
    "reason": "Favorite player scored a goal"
  }
]
```

## 5. Functional Requirements

- Accept a list of events and a preference object.
- Score each event using the rules in Section 6.
- If the preference object includes recognized fields, apply the relevant preference boosts.
- If the preference object is empty or includes no recognized fields, score events based on event type only.
- Return only events with score > 0, sorted highest first.
- Each result includes the original event, its score, and a plain-English reason.

## 6. Scoring Rules

Scores are additive. Matching is case-insensitive.

| Condition                                | Points |
|------------------------------------------|--------|
| Event player matches `favorite_player`   | +8     |
| Event team matches `favorite_team`       | +5     |
| Event type is `goal`                     | +4     |
| Event type is `assist`                   | +3     |
| Event type is `card`                     | +1     |

## 7. Constraints

- No video processing, JSON logic only.
- Self-contained Python module, no external calls or database.

## 8. Edge Cases

| Case | Behavior |
|------|----------|
| Empty events list | Return `[]` |
| No events score above 0 | Return `[]` |
| Event missing `player` or `team` | Ignore missing field, no error |
| Empty preference object | Score based on event type only (no boost) |

## 9. Success Criteria

- Output contains only events with score > 0.
- Output is sorted by score, highest first.
- A goal by the favorite player scores at least 12 (8 + 4).
- An empty events list returns `[]` without error.
- An empty preference results in scoring based on event type only.
