import pytest
from src import safety

def test_crisis_detection_positive():
    detected, reason = safety.check_crisis_indicators("I feel like I want to kill myself tonight")
    assert detected is True
    assert "kill myself" in reason.lower()

def test_crisis_detection_self_harm():
    detected, reason = safety.check_crisis_indicators("I am thinking about self harm and cutting")
    assert detected is True

def test_crisis_detection_negative():
    detected, _ = safety.check_crisis_indicators("I am just feeling tired after studying for exams")
    assert detected is False

def test_crisis_response_india():
    res = safety.get_crisis_response("India")
    assert res["is_crisis"] is True
    assert "Tele-MANAS" in res["message"] or "14416" in res["message"]
    assert "112" in res["emergency"]

def test_crisis_response_us():
    res = safety.get_crisis_response("United States")
    assert res["is_crisis"] is True
    assert "988" in res["message"]
