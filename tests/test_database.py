import pytest
import tempfile
import os
from src import database

@pytest.fixture
def temp_db():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    database.init_db(path)
    yield path
    if os.path.exists(path):
        os.remove(path)

def test_save_and_retrieve_mood(temp_db):
    entry_id = database.save_mood_entry(
        mood_score=4,
        stress_level=2,
        sleep_hours=7.5,
        sleep_quality=4,
        activities="Reading, Outdoors",
        journal_text="Had a refreshing morning walk.",
        db_path=temp_db
    )
    assert entry_id > 0
    
    entries = database.get_all_mood_entries(limit=10, db_path=temp_db)
    assert len(entries) == 1
    assert entries[0]["mood_score"] == 4
    assert entries[0]["sleep_hours"] == 7.5

def test_delete_single_entry(temp_db):
    entry_id = database.save_mood_entry(
        mood_score=3,
        stress_level=3,
        sleep_hours=6.0,
        sleep_quality=3,
        db_path=temp_db
    )
    success = database.delete_mood_entry(entry_id, db_path=temp_db)
    assert success is True
    
    entries = database.get_all_mood_entries(limit=10, db_path=temp_db)
    assert len(entries) == 0

def test_delete_all_data(temp_db):
    database.save_mood_entry(3, 3, 6.0, 3, db_path=temp_db)
    database.save_mood_entry(4, 2, 8.0, 4, db_path=temp_db)
    database.save_screening_result("PHQ-9", 5, 27, "Mild", db_path=temp_db)
    
    database.delete_all_data(db_path=temp_db)
    
    assert len(database.get_all_mood_entries(db_path=temp_db)) == 0
    assert len(database.get_screening_history(db_path=temp_db)) == 0
