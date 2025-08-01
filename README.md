# Project 2 Graphs

Error analysis visualization tool for screenshot task performance data.

## 📁 Directory Structure

```
project2Graphs/
├── data/                    # CSV data files
├── src/                     # Source code
├── knowledge_errors.jpg     # Generated graph: Knowledge-based errors
├── rules_errors.jpg         # Generated graph: Rules-based errors
└── README.md               # This file
```

## 🎯 Purpose

Analyzes user performance data from screenshot tasks, identifying two types of errors:
- **Knowledge errors**: "didn't know", "couldn't find", "no attempt", "IDK", "incorrect"
- **Rules errors**: "was able to get", "First did"

## 📊 Output

Generates side-by-side bar charts comparing:
- Task 4 (screenshot to clipboard) vs Task 5 (screenshot full screen)
- Error counts vs total response counts
- Statistical summaries with error percentages

## 🚀 Usage

1. Place your CSV data in the `data/` folder
2. Run the analysis script from `src/`
3. View generated graphs: `knowledge_errors.jpg` and `rules_errors.jpg`

## 📈 Generated Graphs

- **knowledge_errors.jpg**: Knowledge-based error analysis
- **rules_errors.jpg**: Rules-based error analysis

Both graphs show error rates across Task 4 and Task 5 with value labels and clean styling.
