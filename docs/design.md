# Design: AI Highlight Selector

## 1. Design Goal

Translate the spec into a small, self-contained Python implementation that scores game events against a user preference, filters out irrelevant events, and returns the top highlights with a plain-English reason.

---

## 2. Architecture

Three logical components, each a plain function:

**Event Scoring** — given a single event and a preference, applies the scoring rules and returns a numeric score plus a list of matched rule labels.

**Highlight Selection** — iterates over all events, scores each one, filters out scores of 0, sorts the remainder, and returns the top N.

**Explanation Generation** — converts the list of matched rule labels into a single human-readable sentence.

---

## 3. System Flow

```
events (list)
    │
    ▼
score_event(event, preference)      ← applied per event
    │
    ▼
filter  score == 0                  ← drop irrelevant events
    │
    ▼
sort by score desc, then tie-break
    │
    ▼
take top N
    │
    ▼
generate_reason(event, preference, applied_rules)   ← per highlight
    │
    ▼
highlights (list of {event, score, reason})
```

---

## 4. Main Functions

### `score_event(event, preference) → (int, list[str])`

Applies each scoring rule in order and accumulates points.

- **Input:** a single event dict, a preference dict
- **Output:** `(total_score, applied_rules)` where `applied_rules` is a list of short labels such as `"favorite player"`, `"goal"`
- Missing event fields (`player`, `team`) are silently skipped.

### `generate_reason(event, preference, applied_rules) → str`

Builds a plain-English sentence from the applied rule labels.

- **Input:** event dict, preference dict, list of rule labels
- **Output:** a single string, e.g. `"Favorite player scored a goal"`
- Returns `"No specific reason"` if `applied_rules` is empty (defensive fallback).

### `select_highlights(events, preference) → list[dict]`

Orchestrates the full pipeline.

- **Input:** list of event dicts, preference dict
- **Output:** list of highlight dicts `{event, score, reason}`, sorted by score desc
- Raises `ValueError` if `preference` contains neither `favorite_player` nor `favorite_team`.
- Returns `[]` if `events` is empty or no event scores above 0.

---

## 5. Data Structures

**Event input**
```python
{
    "type":   str,   # required — "goal" | "assist" | "card"
    "player": str,   # optional
    "team":   str,   # optional
    "minute": int    # optional
}
```

**Preference input**
```python
{
    "favorite_player": str,  # optional
    "favorite_team":   str   # optional
    # at least one must be present
}
```

**Highlight output**
```python
{
    "event":  dict,  # original event, unchanged
    "score":  int,   # total score > 0
    "reason": str    # plain-English explanation
}
```

---

## 6. Sorting and Tie-Breaking

Primary sort: `score` descending.

When scores are equal:
1. Prefer `goal` over `assist` over `card` (event type rank).
2. Prefer the earlier `minute` (lower value wins).
3. If `minute` is absent, treat it as `999` (pushed to the end among ties).

---

## 7. Error Handling

| Situation | Behavior |
|-----------|----------|
| `events` is empty | Return `[]` |
| `preference` has no recognized fields | Raise `ValueError("preference must include favorite_player or favorite_team")` |
| Event missing `player` or `team` | Skip the corresponding scoring rule; no error |
| Event has an unrecognized `type` | No type-based points awarded; other rules still apply |

---

## 8. Demo Plan

**Sample input file:** `sample_input.json`

```json
{
  "events": [
    { "type": "goal",   "player": "Messi",  "team": "Inter Miami", "minute": 34 },
    { "type": "assist", "player": "Messi",  "team": "Inter Miami", "minute": 20 },
    { "type": "card",   "player": "Ramos",  "team": "Al Hilal",    "minute": 67 },
    { "type": "goal",   "player": "Suarez", "team": "Inter Miami", "minute": 55 }
  ],
  "preference": {
    "favorite_player": "Messi",
    "favorite_team":   "Inter Miami"
  }
}
```

**Run the demo:**
```bash
python demo.py
```

`demo.py` loads `sample_input.json`, calls `select_highlights(events, preference)`, and prints the results to stdout.

**Expected output** (abbreviated):
```
1. [score 17] Messi goal at 34'  — Favorite player, favorite team, goal
2. [score 16] Messi assist at 20' — Favorite player, favorite team, assist
3. [score 9]  Suarez goal at 55' — Favorite team, goal
```
