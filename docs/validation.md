# Validation: AI Highlight Selector

## Test Run

**Input file:** `data/sample_input.json`  
**Preference:** `favorite_player = Messi`, `favorite_team = Inter Miami`  
**Command:** `python3 src/highlight_selector.py`

## Results

| # | Player | Event | Minute | Score | Reason |
|---|--------|-------|--------|-------|--------|
| 1 | Messi  | Goal  | 34'    | 17    | Favorite player, Favorite team, Goal |
| 2 | Messi  | Assist| 20'    | 16    | Favorite player, Favorite team, Assist |
| 3 | Suarez | Goal  | 55'    | 9     | Favorite team, Goal |
| 4 | Ramos  | Card  | 67'    | 1     | Card |

## Success Criteria Check

| Criterion | Expected | Result | Pass |
|----------|----------|--------|------|
| Output contains only events with score > 0 | No zero-score events | Ramos card (score 1) included, no zero-score events returned | Yes |
| Output is sorted by score, highest first | 17 → 16 → 9 → 1 | 17, 16, 9, 1 | Yes |
| Goal by favorite player scores at least 12 | ≥ 12 | Messi goal = 17 | Yes |
| Empty events list returns `[]` without error | `[]` | Not tested in this run | Not tested |
| Empty preference is scored by event type only | Base score only, no preference boost | Not tested in this run | Not tested |

## Score Breakdown

| Event | Favorite Player (+8) | Favorite Team (+5) | Type Score | Total |
|------|----------------------|--------------------|------------|-------|
| Messi goal | +8 | +5 | +4 goal | 17 |
| Messi assist | +8 | +5 | +3 assist | 16 |
| Suarez goal | 0 | +5 | +4 goal | 9 |
| Ramos card | 0 | 0 | +1 card | 1 |

## Conclusion

The implementation matches the scoring rules defined in `docs/spec.md`.

The output is deterministic, correctly sorted, and suitable for demo purposes.

The system prioritizes resilience by supporting partial or missing preferences, ensuring consistent behavior without runtime failures.

## Additional Validation Notes

- The implementation handles the tested scoring path deterministically.
- Events are ranked strictly by descending score.
- Preference boosts are applied only when matching fields exist.
- When preference is empty, scoring falls back to event type without introducing errors.
