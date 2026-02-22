print("=== Inventory Variance Tracker ===")
print("Type 'done' as the item name to finish.\n")

def check_severity(abs_var, expected_quantity, counted_quantity):
    security_label = None

    # Classify variance type (surplus/deficit/stockout) before applying severity thresholds
    if expected_quantity == counted_quantity:
        type_label = None
    elif expected_quantity == 0 and counted_quantity > 0:
        type_label = "Unexpected surplus"
    elif expected_quantity < counted_quantity:
        type_label = "Surplus"
    elif expected_quantity > 0 and counted_quantity == 0:
        type_label = "Stockout"
    elif expected_quantity > counted_quantity:
        type_label = "Inventory deficit"

    # Only compute percent-based severity when expected > 0 (avoids divide-by-zero)
    if expected_quantity > 0 and type_label:
        percent_off = abs_var / expected_quantity * 100
        if percent_off > 25:
            security_label = "CRITICAL"
        elif percent_off > 12:
            security_label = "HIGH"

    if security_label and type_label != 0:
        return f"{security_label} {type_label}"
    else:
        return type_label


total_items_checked = 0
absolute_variance = 0

over_count = 0
under_count = 0
over_times = 0
under_times = 0

largest_variance = 0
largest_variable_item = ""

largest_over = ""
largest_over_amount = 0

largest_under = ""
largest_under_amount = 0

while True:
    item = input("Item name: ").strip()

    if item == "":
        print("Item name cannot be blank.")
        continue

    if item.lower() == "done":
        break

    # Input validation loop for expected quantity
    while True:
        expected_quantity = input("Expected quantity: ")
        try:
            expected_quantity = int(expected_quantity)
        except ValueError:
            print("That is not a whole number.")
            continue
        if expected_quantity < 0:
            print("Quantity cannot be negative.")
            continue
        break

    while True:
        counted_quantity = input("Counted quantity: ")
        try:
            counted_quantity = int(counted_quantity)
        except ValueError:
            print("That is not a whole number.")
            continue
        if counted_quantity < 0:
            print("Quantity cannot be negative.")
            continue
        break

    total_items_checked += 1

    variance = counted_quantity - expected_quantity
    abs_var = abs(variance)

    alert = check_severity(abs_var, expected_quantity, counted_quantity)
    # Track largest absolute variance seen so far
    if abs_var > largest_variance:
        largest_variance = abs_var
        largest_variable_item = item
    # Update counts and track largest over/under items
    if variance > 0:
        over_times += 1
        over_count += abs_var

        if abs_var > largest_over_amount:
            largest_over = item
            largest_over_amount = abs_var

        print(f"Item: {item} OVER by {variance}")
        if alert:
            print(alert)
    elif variance < 0:
        under_times += 1
        under_count += abs_var

        if abs_var > largest_under_amount:
            largest_under = item
            largest_under_amount = abs_var

        print(f"Item: {item} UNDER by {abs_var}")
        if alert:
            print(alert)
    else:
        print(f"{item}: OK (no variance)")
    print()

    absolute_variance += abs_var

if total_items_checked > 0:
    print("\n=== Summary Report ===")
    print(f"\nTotal items checked: {total_items_checked}")
    print(f"Items with variance: {over_times + under_times}\n")
    print(f"Items with variance over: {over_times}")
    print(f"Items with variance under: {under_times}")
    print(f"Total absolute variance: {absolute_variance}\n")
else:
    print("\n=== No Items Checked ===")

if over_times > 0:
    print(f"Total over: {over_count}")
if under_times > 0:
    print(f"Total under: {under_count}")

if largest_variance > 0:
    print(f"\nLargest variance: {largest_variable_item}, ({largest_variance})")

if largest_under != "":
    print(f"Largest variance under: {largest_under}, {largest_under_amount}")
if largest_over != "":
    print(f"Largest variance over: {largest_over}, {largest_over_amount}")
