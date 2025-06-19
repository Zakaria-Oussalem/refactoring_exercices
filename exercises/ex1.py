"""
This code processes a list of feedback strings, printing them in different formats based on their content.
"""


def main(feedback_list):
    process_feedbacks = []
    for i in range(len(feedback_list)):
        feedback = feedback_list[i]
        if len(feedback) > 0:
            if feedback[0] == "#":
                continue
            if "bad" in feedback or "terrible" in feedback or "awful" in feedback:
                process_feedbacks.append(f"Negative: {feedback.upper()}")
            else:
                process_feedbacks.append(f"Positive: {feedback.lower()}")
    return process_feedbacks
