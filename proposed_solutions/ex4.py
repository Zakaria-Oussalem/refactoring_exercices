from dataclasses import dataclass
from pydantic import BaseModel
from enum import Enum


class Country(str, Enum):
    US = "US"
    CA = "CA"
    UK = "UK"
    AU = "AU"


SHIPPING_BASE_COST = 5.99
HEAVY_ITEM_THRESHOLD = 10
HEAVY_ITEM_EXTRA_COST = 10.0
COUNTRIES_AVAILABLE_FOR_DIGITAL_ITEMS = {"US"}
CREDIT_CARD_FEE = 0.02  # 2% fee for credit card payments

class FatalCheckoutError(Exception):
    """Base class for checkout-related errors."""

    pass


class CheckoutError(Exception):
    """Base class for non-fatal checkout errors."""

    pass


class MissingAddress(FatalCheckoutError):
    pass


class UnavailableProduct(CheckoutError):
    pass


class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"


def pay_with_paypal(user: str, amount: float) -> float:
    print(f"Redirecting {user} to PayPal for ${amount:.2f}")
    return amount


def pay_with_credit_card(user: str, amount: float) -> float:
    print(f"Charging {user} ${amount:.2f} via credit card")
    amount += amount * CREDIT_CARD_FEE
    print(f"Total amount after fees: ${amount:.2f}")
    return amount


PAYMENT_MAPPING = {
    PaymentMethod.CREDIT_CARD: pay_with_credit_card,
    PaymentMethod.PAYPAL: pay_with_paypal,
}


class ItemType(str, Enum):
    DIGITAL = "digital"
    PHYSICAL = "physical"
    SUBSCRIPTION = "subscription"


class User(BaseModel):
    name: str
    country: Country
    address: str | None = None
    active_subscriptions: set[str] = set()


@dataclass
class CartItem:
    name: str
    price: float

    def validate_for_user(self, user: User) -> bool:
        return True

    def calculate_price(self, user: User) -> float:
        return self.price

    def update_user_state(self, user: User) -> None:
        pass


@dataclass
class SubscriptionItem(CartItem):
    subscription_id: str

    def validate_for_user(self, user: User) -> bool:
        if self.subscription_id in user.active_subscriptions:
            print("Skipping subscription — already active")
            return False
        return True

    def calculate_price(self, user: User) -> float:
        print(f"Adding subscription: {self.name}")
        return self.price

    def update_user_state(self, user: User) -> None:
        user.active_subscriptions.add(self.subscription_id)


@dataclass
class DigitalItem(CartItem):
    def validate_for_user(self, user: User) -> bool:
        if user.country not in COUNTRIES_AVAILABLE_FOR_DIGITAL_ITEMS:
            print("Warning: some digital items may not be available outside the US")
            raise UnavailableProduct("Digital item not available in user's country.")
        return True

    def calculate_price(self, user: User) -> float:
        print(f"Adding digital item: {self.name}")
        return self.price


@dataclass
class PhysicalItem(CartItem):
    weight: float

    def __post_init__(self):
        if self.weight <= 0:
            raise ValueError("Weight must be a positive number for physical items.")

    def validate_for_user(self, user: User) -> bool:
        if user.address is None:
            print("Error: Cannot ship physical items without an address")
            raise MissingAddress("User address is required for physical items.")
        return True

    def calculate_shipping(self) -> float:
        shipping = SHIPPING_BASE_COST
        if self.weight > HEAVY_ITEM_THRESHOLD:
            shipping += HEAVY_ITEM_EXTRA_COST
        return shipping

    def calculate_price(self, user: User) -> float:
        shipping = self.calculate_shipping()
        print(f"Adding physical item: {self.name} with shipping {shipping}")
        return self.price + shipping


PRODUCT_CLASSES = {
    ItemType.DIGITAL: DigitalItem,
    ItemType.PHYSICAL: PhysicalItem,
    ItemType.SUBSCRIPTION: SubscriptionItem,
}


def cart_item_factory(data: dict) -> CartItem:
    item_type = data.pop("type", "").lower()

    if item_type not in PRODUCT_CLASSES:
        raise ValueError(f"Unsupported item type: {item_type}")
    return PRODUCT_CLASSES[item_type](**data)


def checkout(cart: list[CartItem], user: User, payment_method: PaymentMethod) -> None:
    total = 0.0

    for item in cart:
        try:
            if not item.validate_for_user(user):
                continue
            total += item.calculate_price(user)
            item.update_user_state(user)
        except CheckoutError as e:
            print(f"Skipping item due to error: {e}")
            continue
        except FatalCheckoutError as e:
            print(f"Fatal error during checkout: {e}")
            return 0.0

    payment_func = PAYMENT_MAPPING.get(payment_method)
    if payment_func:
        new_total = payment_func(user.name, total)
        return new_total
    else:
        print("Unsupported payment method")
        return 0.0


def main(cart: list[dict], user_data: dict, payment_method: str) -> None:
    """Main function to handle the checkout process."""
    cart_items = [cart_item_factory(item) for item in cart]
    user = User(**user_data)
    payment_method = PaymentMethod(payment_method)
    return checkout(cart_items, user, payment_method)


# Example usage
if __name__ == "__main__":
    fetched_cart = [
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
    fetched_user = {
        "name": "Alice",
        "country": "US",
        "address": "123 Main St, Springfield, USA",
        "active_subscriptions": {"111"},
    }
    payment_method = "credit_card"

    main(fetched_cart, fetched_user, payment_method)

# what was done right ?
# ✅ Moodularity and using dataclasses for item representation.
# ✅ Handle different item types and payment methods effectively.
# ✅ Raise appropriate exceptions for errors, allowing for graceful error handling.
# ✅ Use Pydantic for user data validation, ensuring that user data is correctly formatted.
# ✅ Use enums for item types and payment methods improves code readability and maintainability.
# ✅ Leverage polymorphism to handle different item types uniformly.


# next step: Seperate all this code into different files
