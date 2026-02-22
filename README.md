# Inventory Variance Tracker (Python)

A command-line application that detects and classifies inventory discrepancies based on expected vs counted quantities.

## Overview

This tool helps identify and categorize inventory variances into:

- Surplus
- Unexpected Surplus
- Inventory Deficit
- Stockout

It applies configurable percent-based severity thresholds (`HIGH` / `CRITICAL`) and generates a structured summary report.

---

## Design Approach

The program:

- Validates user input to ensure non-negative integers
- Prevents divide-by-zero errors for unexpected inventory
- Separates classification logic from presentation
- Uses named constants to eliminate magic numbers
- Tracks aggregate metrics and largest variance cases

Severity thresholds are configurable through constants, allowing easy adjustment without modifying classification logic.

---

## 🧪 Example Output

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

## What This Demonstrates

- Structured control flow and input validation
- Edge-case handling (stockout and unexpected surplus)
- Threshold-based classification systems
- Incremental refactoring toward production-quality structure

---

## Future Improvements

- Extract reusable input helper functions
- Add unit tests for boundary conditions
- Wrap execution in a `main()` entry point
- Extend to CSV-based inventory ingestion
