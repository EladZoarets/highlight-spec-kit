import json

TYPE_SCORES = {"goal": 4, "assist": 3, "card": 1}
TYPE_RANK   = {"goal": 0, "assist": 1, "card": 2}


def score_event(event, preference):
    """Return (score, applied_rules) for a single event."""
    score = 0
    rules = []

    fav_player = preference.get("favorite_player", "")
    fav_team   = preference.get("favorite_team", "")

    if fav_player and event.get("player", "").lower() == fav_player.lower():
        score += 8
        rules.append("favorite player")

    if fav_team and event.get("team", "").lower() == fav_team.lower():
        score += 5
        rules.append("favorite team")

    event_type = event.get("type", "").lower()
    if event_type in TYPE_SCORES:
        score += TYPE_SCORES[event_type]
        rules.append(event_type)

    return score, rules


def generate_reason(applied_rules):
    """Build a plain-English reason from the list of matched rule labels."""
    if not applied_rules:
        return "No specific reason"
    return ", ".join(r.capitalize() for r in applied_rules)


def select_highlights(events, preference):
    """Score, filter, sort, and return all highlights with score > 0."""
    if not (preference.get("favorite_player") or preference.get("favorite_team")):
        raise ValueError("preference must include favorite_player or favorite_team")

    scored = []
    for event in events:
        score, rules = score_event(event, preference)
        if score > 0:
            scored.append((score, rules, event))

    scored.sort(key=lambda x: (
        -x[0],
        TYPE_RANK.get(x[2].get("type", "").lower(), 99),
        x[2].get("minute", 999),
    ))

    return [
        {"event": event, "score": score, "reason": generate_reason(rules)}
        for score, rules, event in scored
    ]


if __name__ == "__main__":
    input_path = "data/sample_input.json"
    with open(input_path) as f:
        data = json.load(f)

    highlights = select_highlights(data["events"], data["preference"])
    print(json.dumps(highlights, indent=2))
