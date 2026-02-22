CRITICAL_THRESHOLD = 25
HIGH_THRESHOLD = 12


def read_nonnegative_int(prompt):
    """Prompt until user enters a non-negative integer."""
    while True:
        raw_value = input(prompt)
        try:
            value = int(raw_value)
        except ValueError:
            print("That is not a whole number.")
            continue

        if value < 0:
            print("Quantity cannot be negative.")
            continue

        return value


def check_severity(abs_var, expected_quantity, counted_quantity):
    type_label = None
    severity_label = None

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
        if percent_off >= CRITICAL_THRESHOLD:
            severity_label = "CRITICAL"
        elif percent_off >= HIGH_THRESHOLD:
            severity_label = "HIGH"

    if severity_label and type_label is not None:
        return f"{severity_label} {type_label}"
    return type_label


def print_summary(
        total_items_checked,
        over_items,
        under_items,
        absolute_variance,
        over_count,
        under_count,
        largest_variance,
        largest_variance_items,
        largest_under_items,
        largest_under_amount,
        largest_over_items,
        largest_over_amount,
):
    if total_items_checked == 0:
        print("\n=== No Items Checked ===")
        return

    print("\n=== Summary Report ===")
    print(f"\nTotal items checked: {total_items_checked}")
    print(f"Items with variance: {over_items + under_items}\n")
    print(f"Items with variance over: {over_items}")
    print(f"Items with variance under: {under_items}")
    print(f"Total absolute variance: {absolute_variance}\n")

    if over_items > 0:
        print(f"Total over: {over_count}")
    if under_items > 0:
        print(f"Total under: {under_count}")

    if largest_variance > 0:
        print(
            f"\nLargest variance: {', '.join(largest_variance_items)} "
            f"({largest_variance})"
        )

    if largest_under_items:
        print(
            f"Largest variance under: {', '.join(largest_under_items)}, "
            f"{largest_under_amount}"
        )
    if largest_over_items:
        print(
            f"Largest variance over: {', '.join(largest_over_items)}, "
            f"{largest_over_amount}"
        )

def main():
    total_items_checked = 0
    absolute_variance = 0

    over_count = 0
    under_count = 0
    over_items = 0
    under_items = 0

    largest_variance_items = []
    largest_variance = 0

    largest_over_items = []
    largest_over_amount = 0

    largest_under_items = []
    largest_under_amount = 0

    while True:
        item = input("Item name: ").strip()

        if item == "":
            print("Item name cannot be blank.")
            continue

        if item.lower() == "done":
            break

        expected_quantity = read_nonnegative_int("Expected quantity: ")
        counted_quantity = read_nonnegative_int("Counted quantity: ")

        total_items_checked += 1

        variance = counted_quantity - expected_quantity
        abs_var = abs(variance)

        alert = check_severity(abs_var, expected_quantity, counted_quantity)

        # Track Largest absolute variance seen so far
        if abs_var > largest_variance:
            largest_variance = abs_var
            largest_variance_items = [item]
        elif abs_var == largest_variance and abs_var > 0:
            largest_variance_items.append(item)

        # Update counts and track largest over/under items
        if variance > 0:
            over_items += 1
            over_count += abs_var

            if abs_var > largest_over_amount:
                largest_over_items = [item]
                largest_over_amount = abs_var
            elif abs_var == largest_over_amount:
                largest_over_items.append(item)

            print(f"Item: {item} OVER by {variance}")
            if alert:
                print(alert)
        elif variance < 0:
            under_items += 1
            under_count += abs_var

            if abs_var > largest_under_amount:
                largest_under_items = [item]
                largest_under_amount = abs_var
            elif abs_var == largest_under_amount:
                largest_under_items.append(item)

            print(f"Item: {item} UNDER by {abs_var}")
            if alert:
                print(alert)
        else:
            print(f"{item}: OK (no variance)")
        print()

        absolute_variance += abs_var

    print_summary(
        total_items_checked,
        over_items,
        under_items,
        absolute_variance,
        over_count,
        under_count,
        largest_variance,
        largest_variance_items,
        largest_under_items,
        largest_under_amount,
        largest_over_items,
        largest_over_amount,
    )

if __name__ == "__main__":
    main()
