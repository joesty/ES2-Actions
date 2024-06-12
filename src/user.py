from src.timelog import Timelog

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.timelog = []

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def add_timelog(self, timelog:Timelog):
        self.timelog.append(timelog)

    def get_worked_hours(self):
        total = 0
        for timelog in self.timelog:
            total += timelog.get_worked_hours()
        return total
    
    def get_paused_hours(self):
        total = 0
        for timelog in self.timelog:
            total += timelog.get_paused_hours()
        return total
    
    def get_average_worked_hours(self):
        if len(self.timelog) == 0:
            return 0
        return self.get_worked_hours() / len(self.timelog)