from src.user import User
from src.timelog import Timelog

class System:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        self.users.append(User(name, email))

    def get_user(self, email) -> User:
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def get_users(self):
        return self.users
    
    def get_user_timelogs(self, email):
        user = self.get_user(email)
        if user is None:
            return []
        return user.timelog
    
    def add_timelog_to_user(self, email, timelog):
        user = self.get_user(email)
        if user is None:
            return
        user.add_timelog(timelog)

    def get_user_worked_hours(self, email):
        user = self.get_user(email)
        if user is None:
            return 0
        return user.get_worked_hours()
    
    def get_user_paused_hours(self, email):
        user = self.get_user(email)
        if user is None:
            return 0
        return user.get_paused_hours()
    
    def get_user_average_worked_hours(self, email):
        user = self.get_user(email)
        if user is None:
            return 0
        return user.get_average_worked_hours()
    
    def get_user_average_paused_hours(self, email):
        user = self.get_user(email)
        if user is None:
            return 0
        return user.get_average_paused_hours()