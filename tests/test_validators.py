import pytest
from pydantic import ValidationError
from src import validators

def test_valid_mood_entry():
    entry = validators.MoodEntryInput(
        mood_score=4,
        stress_level=2,
        sleep_hours=8.0,
        sleep_quality=4,
        activities="Exercise",
        journal_text="Feeling energized"
    )
    assert entry.mood_score == 4
    assert entry.sleep_hours == 8.0

def test_invalid_mood_score_out_of_range():
    with pytest.raises(ValidationError):
        validators.MoodEntryInput(
            mood_score=6,  # Valid range is 1..5
            stress_level=2,
            sleep_hours=7.0,
            sleep_quality=3
        )

def test_invalid_sleep_hours():
    with pytest.raises(ValidationError):
        validators.MoodEntryInput(
            mood_score=3,
            stress_level=2,
            sleep_hours=-1.0,  # Negative sleep
            sleep_quality=3
        )

def test_valid_screening_answers():
    val = validators.ScreeningResponseInput(
        instrument="PHQ-9",
        answers=[0, 1, 2, 3, 0, 1, 2, 3, 0]
    )
    assert len(val.answers) == 9

def test_invalid_screening_score():
    with pytest.raises(ValidationError):
        validators.ScreeningResponseInput(
            instrument="PHQ-9",
            answers=[0, 1, 4]  # 4 is not an allowed score in PHQ-9 (0..3)
        )
