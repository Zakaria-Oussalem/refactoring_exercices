def calculate_discount(price: float, discount_rate: float) -> float:
    """Calculate the discount amount and return the final price."""
    return price * (1 - discount_rate)


def display_discount(product_type: str, discount: float) -> None:
    """Display the discount amount for the product."""
    print(f"{product_type.capitalize()} Discount: ${discount:.2f}")


DISCOUNTS_RATE_MAPPING: dict[str, float] = {
    "electronics": 0.10,
    "clothing": 0.15,
    "books": 0.05,
}


def main(product: dict) -> float:
    """Apply the appropriate discount based on product category."""
    product_type = product["category"]
    price = product["price"]
    rate = DISCOUNTS_RATE_MAPPING.get(product_type)

    if rate is not None:
        final_price = calculate_discount(price, rate)
        display_discount(product_type, price - final_price)
        return final_price
    else:
        print("No discount available.")
        return price


# ✅ Extract the calculate discount function logic into a separate function
# ✅ Use a dictionary to map product categories to discount rates
