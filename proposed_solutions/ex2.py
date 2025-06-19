import numbers


def keep_numbers_only(data: list) -> list[numbers.Number]:
    """Filter out non-numeric values from the list."""
    return [item for item in data if isinstance(item, numbers.Number)]


def display_numbers(data: list[numbers.Number]):
    """Display the numeric values."""
    for val in data:
        print(val)


def main(data: list) -> list[numbers.Number]:
    numeric_only = keep_numbers_only(data)
    sorted_numbers = sorted(numeric_only)
    display_numbers(sorted_numbers)
    return sorted_numbers


# ✅ use list comprehension to filter out non-numeric values
# ✅ use built-in sorted function to sort the list and using numbers.Number to check for numeric types
# ✅ extracting functions to respect single responsibility principle
