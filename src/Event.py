class Event:
    startTime = 0
    duration = 0
    endTime = 0


    # Create an event starting at startTime minutes from midnight, that is duration minutes long
    def __init__(self, startTime, duration) -> None:
        self.startTime = startTime
        self.duration = duration
        self.endTime = duration + startTime

