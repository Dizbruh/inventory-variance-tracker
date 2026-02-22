# Inventory Variance Tracker (Python)

A command-line Python application that compares expected and counted inventory quantities and classifies the result as:

- Surplus  
- Unexpected Surplus  
- Inventory Deficit  
- Stockout  

The tool applies configurable percent-based severity thresholds (`HIGH` / `CRITICAL`) and generates a structured summary report.

---

## 🚀 Features

- Interactive CLI workflow
- Input validation for non-negative integers
- Variance classification logic
- Percent-based severity thresholds (configurable via constants)
- Divide-by-zero protection for unexpected inventory
- Tie-aware tracking of largest variances
- Aggregated summary reporting
- Modular structure using helper functions and `main()` entry point

---

## 🧠 Design Highlights

- Classification logic is separated from presentation logic.
- Severity thresholds are defined as named constants to eliminate magic numbers.
- Edge cases (stockout, unexpected surplus, zero variance) are handled explicitly.
- Helper functions reduce duplication and improve maintainability.
- Execution is wrapped in a `main()` function with an `if __name__ == "__main__":` guard for clean module behavior.

---

## 🧪 Example Run

```
Item: Widget OVER by 15
CRITICAL Surplus

Item: Bolts UNDER by 4
HIGH Inventory deficit

=== Summary Report ===
Total items checked: 2
Items with variance: 2
Items with variance over: 1
Items with variance under: 1
Total absolute variance: 19
```

---

## 🔧 Configuration

Severity thresholds are defined at the top of the script:

```python
CRITICAL_THRESHOLD = 25
HIGH_THRESHOLD = 12
```

Adjust these values to change classification sensitivity.

---

## 📌 Future Improvements

- Add unit tests for boundary and edge cases
- Support CSV file input/output
- Persist inventory results to disk
- Expand into a file-based reconciliation tool

---

## 🛠 Tech Stack

- Python 3
- Standard Library only
- Command-Line Interface (CLI)

---

## 📖 What This Project Demonstrates

- Structured control flow and state tracking
- Defensive programming practices
- Edge-case reasoning
- Threshold-based classification systems
- Incremental refactoring toward production-style structure
