# Inventory Variance Tracker (CLI)

A command-line inventory reconciliation tool built in Python.

Enter expected and counted quantities for items, then generate a structured summary report highlighting discrepancies, severity levels, and the largest over/under variances.

Built after Parts 1–3 of the University of Helsinki Python MOOC and refactored in Version 2 to improve structure and reporting clarity.

---

## Features

- Input validation for non-negative integers
- Detects:
  - Surplus
  - Inventory deficit
  - Stockout
  - Unexpected surplus
- Severity classification using percentage-based thresholds
- Tie-handling for largest over/under variances
- Clean summary reporting
- Clear output when all items match expected quantities

---

## Version 2 Improvements

- Replaced parallel lists with a dictionary-based `records` data model
- Eliminated index alignment bugs (alerts and item data cannot drift)
- Refactored summary calculations into a dedicated `compute_summary(records)` pass
- Simplified summary control flow and removed unreachable logic
- Standardized output formatting and spacing
- Removed unused tracking state to reduce cognitive load

---

## Design Notes

- Uses a single `records` list of dictionaries as the source of truth
- Each record contains:
  - `name`
  - `expected`
  - `counted`
  - `variance`
  - `abs_var`
  - `alert` (or `None`)
- Summary metrics are derived by scanning `records` (counts, totals, largest over/under with ties)
- Severity classification avoids divide-by-zero by only applying percentage thresholds when `expected > 0`

---

## How to Run

```bash
python3 inventory_tracker.py
```

Type `done` when finished entering items to generate the summary report.

---

## Example Output

```text
=== Summary Report ===

Total items checked: 2
Items and counts:

Item name: Milk | Variance: 5
Expected: 10 | Counted: 15
Alert: HIGH Surplus

Item name: Eggs | Variance: 0
Expected: 12 | Counted: 12

======================

Items with variance over: 1
Items with variance under: 0

Largest over variance: Milk by 5
```

---

## Future Improvements

- Add financial impact estimates (price per item × variance)
- Export report to file (CSV or text)
- Sorting options for report output
- Optional reorder-point flagging

---

## Why This Project

This project demonstrates:

- Input validation
- Conditional logic and classification
- Loop-based data entry and reporting
- Refactoring discipline
- Data structure evolution (parallel lists → record dictionaries)
- Business-oriented summary output