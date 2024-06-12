import pytest
from datetime import datetime, timedelta
from src.timelog import Timelog

@pytest.fixture
def timelog():
    return Timelog()

def test_start_and_end_work(timelog):
    start_time = datetime(2023, 1, 1, 8, 0)
    end_time = datetime(2023, 1, 1, 16, 0)
    timelog.start_work(start_time)
    timelog.end_work(end_time)
    assert timelog.get_worked_hours() == 8

def test_start_and_end_pause(timelog):
    start_time = datetime(2023, 1, 1, 12, 0)
    end_time = datetime(2023, 1, 1, 13, 0)
    timelog.start_pause(start_time)
    timelog.end_pause(end_time)
    assert timelog.get_paused_hours() == 1

def test_worked_hours_with_no_start_or_end_time(timelog):
    assert timelog.get_worked_hours() == 0

def test_paused_hours_with_no_start_or_end_time(timelog):
    assert timelog.get_paused_hours() == 0

def test_worked_hours_with_no_end_time(timelog):
    start_time = datetime(2023, 1, 1, 8, 0)
    timelog.start_work(start_time)
    assert timelog.get_worked_hours() == 0

def test_paused_hours_with_no_end_time(timelog):
    start_time = datetime(2023, 1, 1, 12, 0)
    timelog.start_pause(start_time)
    assert timelog.get_paused_hours() == 0

def test_worked_hours_with_no_start_time(timelog):
    end_time = datetime(2023, 1, 1, 16, 0)
    timelog.end_work(end_time)
    assert timelog.get_worked_hours() == 0

def test_paused_hours_with_no_start_time(timelog):
    end_time = datetime(2023, 1, 1, 13, 0)
    timelog.end_pause(end_time)
    assert timelog.get_paused_hours() == 0

def test_worked_hours_with_end_time_before_start_time(timelog):
    start_time = datetime(2023, 1, 1, 16, 0)
    end_time = datetime(2023, 1, 1, 8, 0)
    timelog.start_work(start_time)
    timelog.end_work(end_time)
    assert timelog.get_worked_hours() == 0

def test_paused_hours_with_end_time_before_start_time(timelog):
    start_time = datetime(2023, 1, 1, 13, 0)
    end_time = datetime(2023, 1, 1, 12, 0)
    timelog.start_pause(start_time)
    timelog.end_pause(end_time)
    assert timelog.get_paused_hours() == 0

    