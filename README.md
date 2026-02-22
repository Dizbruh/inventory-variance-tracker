# Inventory Variance Tracker

A command-line Python application that tracks inventory discrepancies and classifies them into:

- Surplus  
- Unexpected Surplus  
- Inventory Deficit  
- Stockout  

Includes percent-based severity levels (HIGH / CRITICAL) and summary reporting.

## Features

- Input validation
- Divide-by-zero protection
- Variance classification logic
- Percent-based severity thresholds
- Largest variance tracking
- Summary report generation

## Tech

- Python 3
- CLI-based interface


## Sample output
Item: Widget OVER by 15
CRITICAL Surplus

=== Summary Report ===
Total items checked: 4
Items with variance: 3
...
