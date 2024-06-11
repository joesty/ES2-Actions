class Timelog:
    def __init__(self) -> None:
        self.workStartTime = None
        self.workEndTime = None
        self.pauseStartTime = None
        self.pauseEndTime = None

    def start_work(self, time):
        self.workStartTime = time

    def end_work(self, time):
        self.workEndTime = time

    def start_pause(self, time):
        self.pauseStartTime = time

    def end_pause(self, time):
        self.pauseEndTime = time

    def get_worked_hours(self):
        if self.workStartTime is None or self.workEndTime is None:
            return 0
        return self.workEndTime - self.workStartTime
    
    def get_paused_hours(self):
        if self.pauseStartTime is None or self.pauseEndTime is None:
            return 0
        return self.pauseEndTime - self.pauseStartTime