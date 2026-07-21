# Spending Personality Analyser

A Python CLI app that tracks your monthly expenses and analyses
your spending behaviour to assign you a personality type.

## What it does
- Add expenses with category, amount, note, and date
- View all expenses with a formatted summary
- Analyse spending patterns across categories
- Assign a spending personality (Comfort Seeker, Impulse Buyer, etc.)
- Save a formatted report as a .txt file
- Persists all data to JSON between sessions

## How to run
1. Clone the repository
2. Open in PyCharm or any Python editor
3. Run `main.py`
4. No external libraries needed — pure Python only

## Project structure
- `main.py`     — entry point and menu loop
- `tracker.py`  — expense input, validation, OOP class
- `analyser.py` — grouping, percentages, personality engine
- `report.py`   — formatted terminal report and file saving
- `data/`       — JSON data files
- `reports/`    — saved report txt files

## What I learned
- Modular Python project structure across multiple files
- File I/O with JSON for data persistence
- Input validation with try/except and while loops
- Dictionary operations and list comprehensions
- OOP with classes, `__init__`, and methods
- f-string formatting for clean terminal output

## Tech used
Python 3.14 — no external dependencies