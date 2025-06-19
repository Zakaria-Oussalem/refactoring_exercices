NEGATIVE_FEEDBACK_KEYWORDS = ["bad", "terrible", "awful"]


def get_negative_feedback(feedback: str) -> str:
    return f"Negative: {feedback.upper()}"


def get_positive_feedback(feedback: str) -> str:
    return f"Positive: {feedback.lower()}"


RESPONSE_MAP = {"NEGATIVE": get_negative_feedback, "POSITIVE": get_positive_feedback}


def main(feedback_list: list) -> list:
    """Process a list of feedback strings and categorize them as positive or negative.
    Args:
        feedback_list (list): A list of feedback strings to process.
    Returns:
        list: A list of processed feedback strings categorized as positive or negative.
    """
    processed_feedback = []
    for feedback in feedback_list:
        if not feedback or feedback[0] == "#":
            continue
        normalized_feedback = feedback.lower()
        if any(
            negative_word in normalized_feedback
            for negative_word in NEGATIVE_FEEDBACK_KEYWORDS
        ):
            processed_feedback.append(RESPONSE_MAP["NEGATIVE"](feedback))
        else:
            processed_feedback.append(RESPONSE_MAP["POSITIVE"](feedback))
    return processed_feedback


# ✅ First Change: loop through the list directly instead of using range(len())
# ✅ Second Change: use any() to check for negative keywords and grouped into a const - reduce lenght and group similar checks
# ✅ Third Change: use not feedback or feedback[0] == '#' to check for empty strings or comments to reduce indentations
# ✅ Fourth Change: used functions to handle different feedback types. and a dictionnary for mapping logic
