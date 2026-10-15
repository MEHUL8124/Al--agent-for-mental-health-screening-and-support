import pytest
from src import screening

def test_phq9_minimal_score():
    answers = [0] * 9
    res = screening.score_phq9(answers)
    assert res["total_score"] == 0
    assert res["severity"] == "Minimal or None"
    assert res["safety_alert"] is False

def test_phq9_severe_score():
    answers = [3] * 9
    res = screening.score_phq9(answers)
    assert res["total_score"] == 27
    assert res["severity"] == "Severe"
    assert res["safety_alert"] is True

def test_phq9_question_9_safety_trigger():
    # Only Question 9 is positive (score = 1), total score = 1 (normally minimal)
    answers = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    res = screening.score_phq9(answers)
    assert res["total_score"] == 1
    assert res["safety_alert"] is True  # Must trigger safety alert!

def test_phq9_invalid_length():
    with pytest.raises(ValueError):
        screening.score_phq9([0] * 8)

def test_gad7_minimal_score():
    answers = [0] * 7
    res = screening.score_gad7(answers)
    assert res["total_score"] == 0
    assert res["severity"] == "Minimal Anxiety"

def test_gad7_severe_score():
    answers = [3] * 7
    res = screening.score_gad7(answers)
    assert res["total_score"] == 21
    assert res["severity"] == "Severe Anxiety"

def test_gad7_invalid_length():
    with pytest.raises(ValueError):
        screening.score_gad7([0] * 6)
