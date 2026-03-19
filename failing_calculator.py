def average_ratios(numbers):
    """
    Calculate the average of ratios (100 divided by each number in the list),
    skipping zero values to avoid division by zero.

    Args:
        numbers (list of float): A list of numbers.

    Returns:
        float: The average of the calculated ratios, or 0 if no valid numbers exist.
    """
    total = 0
    count = 0

    for number in numbers:
        if number == 0:
            continue  # Skip zero to avoid division by zero
        total += 100 / number
        count += 1

    if count == 0:
        return 0  # Return 0 if all numbers are zero or skipped

    return total / count

print(average_ratios([10, 5, 0]))
