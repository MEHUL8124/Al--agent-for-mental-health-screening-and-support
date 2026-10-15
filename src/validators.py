from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class MoodEntryInput(BaseModel):
    mood_score: int = Field(..., ge=1, le=5, description="Mood score from 1 (very low) to 5 (great)")
    stress_level: int = Field(..., ge=1, le=5, description="Stress level from 1 (low) to 5 (extreme)")
    sleep_hours: float = Field(..., ge=0.0, le=24.0, description="Hours of sleep in past 24h")
    sleep_quality: int = Field(..., ge=1, le=5, description="Sleep quality from 1 (poor) to 5 (restful)")
    activities: Optional[str] = Field(default="", max_length=200)
    journal_text: Optional[str] = Field(default="", max_length=2000)

    @field_validator("journal_text")
    @classmethod
    def clean_journal_text(cls, v: Optional[str]) -> str:
        if v is None:
            return ""
        return v.strip()

class ScreeningResponseInput(BaseModel):
    instrument: str = Field(..., description="Screening instrument name e.g. PHQ-9 or GAD-7")
    answers: List[int] = Field(..., description="List of item scores from 0 to 3")

    @field_validator("answers")
    @classmethod
    def validate_answers(cls, v: List[int]) -> List[int]:
        if not v:
            raise ValueError("Answers list cannot be empty.")
        for score in v:
            if score not in (0, 1, 2, 3):
                raise ValueError(f"Invalid answer score {score}. Allowed values are 0, 1, 2, 3.")
        return v

class ChatMessageInput(BaseModel):
    user_message: str = Field(..., min_length=1, max_length=1500)

    @field_validator("user_message")
    @classmethod
    def validate_message(cls, v: str) -> str:
        trimmed = v.strip()
        if not trimmed:
            raise ValueError("Message cannot be empty.")
        return trimmed
