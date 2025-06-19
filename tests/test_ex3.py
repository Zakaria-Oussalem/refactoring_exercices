import pytest
from exercises.ex3 import main as exercice
from proposed_solutions.ex3 import main as solution
from your_solutions.ex3 import main as your_solution

PRODUCTS = [
    {"name": "Laptop", "price": 1000.00, "category": "electronics"},
    {"name": "T-Shirt", "price": 20.00, "category": "clothing"},
    {"name": "Novel", "price": 15.00, "category": "books"},
    {"name": "Unknown Item", "price": 50.00, "category": "unknown"},
]

EXPECTED_OUTPUT = [
    900.00,  # Electronics discount
    17.00,  # Clothing discount
    14.25,  # Books discount
    50.00,  # No discount for unknown category
]


def test_exercice():
    results = [exercice(product) for product in PRODUCTS]
    assert results == EXPECTED_OUTPUT, (
        "Exercise function did not return expected results"
    )


def test_solution():
    results = [solution(product) for product in PRODUCTS]
    assert results == EXPECTED_OUTPUT, (
        "Solution function did not return expected results"
    )


def test_your_solution():
    results = [your_solution(product) for product in PRODUCTS]
    assert results == EXPECTED_OUTPUT, "Your solution did not return expected results"
