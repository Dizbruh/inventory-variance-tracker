CRITICAL_THRESHOLD = 25
HIGH_THRESHOLD = 12


def read_item(prompt):
    """Prompt until user enters "done"."""
    while True:
        item = input(prompt).strip()

        if item == "":
            print("Item name cannot be blank.\n")
            continue

        return item


def read_non_negative_int(prompt):
    """Prompt until user enters a non-negative integer."""
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("That is not a whole number.\n")
            continue

        if value < 0:
            print("Quantity cannot be negative.\n")
            continue

        return value


def compute_summary(records):
    over_items = 0
    under_items = 0
    large_over_amount = 0
    large_under_amount = 0
    large_over_items = []
    large_under_items = []
    absolute_var = 0

    for record in records:
        name = record["name"]
        abs_var = record["abs_var"]
        variance = record["variance"]
        absolute_var += abs_var

        if variance > 0:
            over_items += 1
            if abs_var > large_over_amount:
                large_over_amount = abs_var
                large_over_items = [name]
            elif abs_var == large_over_amount:
                large_over_items.append(name)

        elif variance < 0:
            under_items += 1
            if abs_var > large_under_amount:
                large_under_amount = abs_var
                large_under_items = [name]
            elif abs_var == large_under_amount:
                large_under_items.append(name)

    return absolute_var, over_items, under_items, large_over_items, large_under_items, large_over_amount, large_under_amount


def check_severity(abs_var, expected_quantity, counted_quantity):
    type_label = None
    severity_label = None

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

    if expected_quantity > 0 and type_label:
        percent_off = abs_var / expected_quantity * 100
        if percent_off >= CRITICAL_THRESHOLD:
            severity_label = "CRITICAL"
        elif percent_off >= HIGH_THRESHOLD:
            severity_label = "HIGH"

    if severity_label and type_label:
        return f"{severity_label} {type_label}"
    return type_label


def print_summary(records):
    if not records:
        print()
        print("=== No Items Checked ===")
        return

    print()
    print("=== Summary Report ===")
    print()
    print(f"Total items checked: {len(records)}")
    print(f"Items and counts:")
    print()

    for record in records:
        print(
            f"Item name: {record['name']} | Variance: {record['abs_var']}\n"
            f"Expected: {record['expected']} | Counted: {record['counted']}"
        )
        if record.get("alert"):
            print(f"Alert: {record['alert']}")
        print()
    print("======================")
    print()

    (
        absolute_var,
        over_items,
        under_items,
        largest_over_items,
        largest_under_items,
        largest_over_amount,
        largest_under_amount,
    ) = compute_summary(records)

    if absolute_var == 0:
        print("All items matched expected quantities.")
    else:
        print(f"Items with variance over: {over_items}")
        print(f"Items with variance under: {under_items}")
        print()

        if largest_under_amount > 0:
            print(
                f"Largest under variance: "
                f"{' | '.join(largest_under_items)} by {largest_under_amount}"
            )

        if largest_over_amount > 0:
            print(
                f"Largest over variance: "
                f"{' | '.join(largest_over_items)} by {largest_over_amount}"
            )
    return


def main():
    records = []

    while True:
        item = read_item("Item name: ")
        if item.lower() == "done":
            break
        expected_quantity = read_non_negative_int("Expected quantity: ")
        counted_quantity = read_non_negative_int("Counted quantity: ")

        variance = counted_quantity - expected_quantity
        abs_var = abs(variance)
        print()

        alert = check_severity(abs_var, expected_quantity, counted_quantity)

        record = {
            "name": item,
            "expected": expected_quantity,
            "counted": counted_quantity,
            "variance": variance,
            "abs_var": abs_var,
            "alert": alert,
        }
        records.append(record)

    print_summary(records)


if __name__ == "__main__":
    main()
