from src.user import User
from src.timelog import Timelog
from datetime import datetime
if __name__ == "__main__":
    user = User("Joao", "email@email.com")
    timelog = Timelog()
    timelog.start_work(datetime(2023, 1, 1, 8, 0))
    timelog.end_work(datetime(2023, 1, 1, 16, 0))
    user.add_timelog(timelog)
    print(user.get_worked_hours())


