import pytest
from src.system import System
from src.user import User
from src.timelog import Timelog
from datetime import datetime
@pytest.fixture
def system():
    return System()

@pytest.fixture
def user():
    return User("John Doe", "john@example.com")

@pytest.fixture
def timelog():
    return Timelog()

def test_add_user(system, user):
    system.add_user(user.name, user.email)
    assert len(system.get_users()) == 1
    assert system.get_users()[0].name == "John Doe"
    assert system.get_users()[0].email == "john@example.com"

def test_get_user(system, user):
    system.add_user(user.name, user.email)
    retrieved_user = system.get_user("john@example.com")
    assert retrieved_user is not None
    assert retrieved_user.email == "john@example.com"

def test_get_user_timelogs(system, user, timelog):
    system.add_user(user.name, user.email)
    system.add_timelog_to_user(user.email, timelog)
    timelogs = system.get_user_timelogs("john@example.com")
    assert len(timelogs) == 1

def test_add_timelog_to_user(system, user, timelog):
    system.add_user(user.name, user.email)
    system.add_timelog_to_user(user.email, timelog)
    assert len(system.get_user_timelogs("john@example.com")) == 1

def test_get_user_worked_hours(system:System, user:User, timelog:Timelog):
    system.add_user(user.name, user.email)
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))    
    system.add_timelog_to_user(user.email, timelog)
    assert system.get_user_worked_hours(user.email) == 8

def test_get_user_paused_hours(system:System, user:User, timelog:Timelog):
    system.add_user(user.name, user.email)
    timelog.start_pause(datetime(2023, 1, 1, 12, 0))
    timelog.end_pause(datetime(2023, 1, 1, 13, 0))    
    system.add_timelog_to_user(user.email, timelog)
    assert system.get_user_paused_hours(user.email) == 1

def test_get_user_average_worked_hours(system:System, user:User, timelog:Timelog):
    system.add_user(user.name, user.email)
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))    
    system.add_timelog_to_user(user.email, timelog)
    assert system.get_user_average_worked_hours(user.email) == 8

def test_get_user_average_paused_hours(system:System, user:User, timelog:Timelog):
    system.add_user(user.name, user.email)
    timelog.start_pause(datetime(2023, 1, 1, 12, 0))
    timelog.end_pause(datetime(2023, 1, 1, 13, 0))    
    system.add_timelog_to_user(user.email, timelog)
    assert system.get_user_average_paused_hours(user.email) == 1
    