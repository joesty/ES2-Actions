import pytest
from datetime import datetime
from src.timelog import Timelog
from src.user import User


@pytest.fixture
def timelog():
    return Timelog()

@pytest.fixture
def user():
    return User("Joao", "email@email.com")

def test_user_name(user):
    assert user.name == "Joao"

def test_user_email(user):
    assert user.email == "email@email.com"

def test_get_paused_hours(user:User):
    assert user.get_paused_hours() == 0

def test_get_worked_hours(user:User):
    assert user.get_worked_hours() == 0

def test_get_average_worked_hours(user:User):
    assert user.get_average_worked_hours() == 0

def test_add_timelog(user:User, timelog:Timelog):
    user.add_timelog(timelog)
    assert len(user.timelog) == 1

def test_get_worked_hours_with_one_timelog(user:User, timelog:Timelog):
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))
    user.add_timelog(timelog)
    assert user.get_worked_hours() == 8

def test_get_paused_hours_with_one_timelog(user:User, timelog:Timelog):
    timelog.start_pause(datetime(2023, 1, 1, 12, 0))
    timelog.end_pause(datetime(2023, 1, 1, 13, 0))
    user.add_timelog(timelog)
    assert user.get_paused_hours() == 1

def test_get_average_worked_hours_with_one_timelog(user:User, timelog:Timelog):
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))
    user.add_timelog(timelog)
    assert user.get_average_worked_hours() == 8

def test_get_worked_hours_with_two_timelogs_with_different_hours(user:User, timelog:Timelog):
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))
    user.add_timelog(timelog)
    timelog = Timelog()
    timelog.start_work(datetime(2023, 1, 2, 8, 0))
    timelog.end_work(datetime(2023, 1, 2, 18, 0))
    user.add_timelog(timelog)
    assert user.get_worked_hours() == 18

def test_get_paused_hours_with_two_timelogs_with_different_hours(user:User, timelog:Timelog):
    timelog.start_pause(datetime(2023, 1, 1, 12, 0))
    timelog.end_pause(datetime(2023, 1, 1, 13, 0))
    user.add_timelog(timelog)
    timelog = Timelog()
    timelog.start_pause(datetime(2023, 1, 2, 12, 0))
    timelog.end_pause(datetime(2023, 1, 2, 13, 0))
    user.add_timelog(timelog)
    assert user.get_paused_hours() == 2

def test_get_average_worked_hours_with_two_timelogs_with_different_hours(user:User, timelog:Timelog):
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))
    user.add_timelog(timelog)
    timelog = Timelog()
    timelog.start_work(datetime(2023, 1, 2, 8, 0))
    timelog.end_work(datetime(2023, 1, 2, 18, 0))
    user.add_timelog(timelog)
    assert user.get_average_worked_hours() == 9
