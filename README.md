# Highlight Selection – Spec Kit Approach

This project implements a highlight selection feature using a Spec-Driven Development (Spec Kit) approach.

The system ranks football match events based on user preferences.

This repository is part of the Generative AI Evangelist assignment.

## Scoring Rules

Base scores:

- goal = 4
- assist = 3
- card = 1

Preference boosts:

- favorite player +8
- favorite team +5

## Architecture

Events Input  
↓  
Scoring Engine  
↓  
Filtering  
↓  
Sorting  
↓  
Highlights Output  

## Run

```bash
python src/highlight_selector.py
