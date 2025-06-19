import pytest
from exercises.ex4 import main as exercise
from proposed_solutions.ex4 import main as solution
from your_solutions.ex4 import main as your_solution


user = {
    "name": "Alice",
    "country": "US",
    "address": "somewhere in the US",
    "active_subscriptions": {"111"},
}

TEST_DATA = [
    (
        [
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
        ],
        {
            "name": "Alice",
            "country": "US",
            "address": "somewhere in the US",
            "active_subscriptions": {"111"},
        },
        "credit_card",
        39.74,
    ),
    (
        [
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
        ],
        {
            "name": "Alice",
            "country": "US",
            "address": "somewhere in the US",
            "active_subscriptions": {"111"},
        },
        "paypal",
        38.96,
    ),
]


@pytest.mark.parametrize("cart,user_data,payment_method,expected_total", TEST_DATA)
def test_main_return_value(cart, user_data, payment_method, expected_total):
    result = exercise(cart, user_data, payment_method)
    assert result == pytest.approx(expected_total, abs=0.01)


@pytest.mark.parametrize("cart,user_data,payment_method,expected_total", TEST_DATA)
def test_solution_return_value(cart, user_data, payment_method, expected_total):
    result = solution(cart, user_data, payment_method)
    assert result == pytest.approx(expected_total, abs=0.01)


@pytest.mark.parametrize("cart,user_data,payment_method,expected_total", TEST_DATA)
def test_your_solution_return_value(cart, user_data, payment_method, expected_total):
    result = your_solution(cart, user_data, payment_method)
    assert result == pytest.approx(expected_total, abs=0.01)
