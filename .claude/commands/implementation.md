Read the project files:

@assignment.md
@spec.md
@design.md


Now implement the AI Highlight Selector according to the specification and design.

Create the following files:

src/highlight_selector.py  
data/sample_input.json

Requirements:
- follow the scoring rules from spec.md
- ignore events with score = 0
- sort events by score (descending)
- return highlights with score and reason
- keep the implementation small and readable

The script should:
1. load data/sample_input.json
2. compute highlights
3. print the result as formatted JSON

Return the full content of both files.