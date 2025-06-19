"""
This code simulates a checkout process for an e-commerce platform.
It handles different types of items in the cart, applies appropriate rules for digital and physical items, and processes subscriptions. It also manages user information and payment methods."""


def main(cart, user, payment_method):
    total = 0
    for item in cart:
        if item["type"] == "digital":
            if user.get("country") != "US":
                print("Warning: some digital items may not be available outside the US")
                continue
            price = item["price"]
            print(f"Adding digital item: {item['name']}")
            total += price
        elif item["type"] == "physical":
            price = item["price"]
            shipping = 5.99
            if item.get("weight", 0) > 10:
                shipping += 10
            print(f"Adding physical item: {item['name']} with shipping {shipping}")
            total += price + shipping
            if user.get("address") is None:
                print("Error: Cannot ship physical items without an address")
                return
        elif item["type"] == "subscription":
            if item["subscription_id"] in user.get("active_subscriptions", set()):
                print("Skipping subscription — already active")
                continue
            price = item["price"]
            print(f"Adding subscription: {item['name']}")
            total += price
            user["active_subscriptions"].add(item["subscription_id"])
        else:
            print(f"Unknown item type: {item['type']}")
            continue

    if payment_method == "credit_card":
        print(f"Charging {user['name']} ${total:.2f} via credit card")
        print(f"Total amount after fees: ${total * 1.02:.2f}")
        return total * 1.02
    elif payment_method == "paypal":
        print(f"Redirecting {user['name']} to PayPal for ${total:.2f}")
        return total
    else:
        print("Unsupported payment method")
        return 0.0


# Example usage
if __name__ == "__main__":
    cart = [
        {"type": "digital", "name": "E-book", "price": 9.99},
        {"type": "physical", "name": "T-shirt", "price": 19.99, "weight": 0.5},
        {
            "type": "subscription",
            "name": "Monthly Magazine",
            "price": 4.99,
            "subscription_id": "111",
        },
        {
            "type": "subscription",
            "name": "Weekly Newsletter",
            "price": 2.99,
            "subscription_id": "222",
        },
    ]
    user = {
        "name": "Alice",
        "country": "US",
        "address": "somewhere in the US",
        "active_subscriptions": {"111"},
    }
    payment_method = "credit_card"

    main(cart, user, payment_method)
