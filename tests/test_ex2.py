from exercises.ex2 import main as exercice
from proposed_solutions.ex2 import main as solution
from your_solutions.ex2 import main as your_solution
import pytest


DATA = [10, 3.5, 2, 7, "a", None, 4, "b", 1.1, "test"]
EXPECTED_OUTPUT = [1.1, 2, 3.5, 4, 7, 10]


def test_exercice():
    result = exercice(DATA)
    assert result == EXPECTED_OUTPUT


def test_solution():
    result = solution(DATA)
    assert result == EXPECTED_OUTPUT


def test_your_solution():
    result = your_solution(DATA)
    assert result == EXPECTED_OUTPUT
