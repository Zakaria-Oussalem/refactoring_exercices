from exercises.ex1 import main as exercise
from proposed_solutions.ex1 import main as solution
from your_solutions.ex1 import main as your_solution
import pytest


FEEDBACK_LIST = [
    "Great job!",
    "bad experience",
    "This was TERRIBLE",
    "Awesome service",
    "# This is a comment",
    "awful product",
    "",
    "Nice work",
]
EXPECTED_OUTPUT = [
    "Positive: great job!",
    "Negative: BAD EXPERIENCE",
    "Negative: THIS WAS TERRIBLE",
    "Positive: awesome service",
    "Negative: AWFUL PRODUCT",
    "Positive: nice work",
]


def test_process_feedback():
    result = exercise(FEEDBACK_LIST)
    assert result == EXPECTED_OUTPUT


def test_process_feedback_solution():
    result = solution(FEEDBACK_LIST)
    assert result == EXPECTED_OUTPUT


def test_process_your_solution():
    result = your_solution(FEEDBACK_LIST)
    assert result == EXPECTED_OUTPUT, "Your solution should match the proposed solution"
