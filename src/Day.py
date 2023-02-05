import Event


class Day:
    events = []
    tasks = []
    schedule = []
    interval = 15  # how many minutes each index in an array takes

    # Require: events is a list of events
    #           tasks are a list of tasks
    def __init__(self, events, tasks) -> None:
        self.events = events
        self.tasks = tasks

        # creating the
        for i in range(1140 // self.interval):
            self.schedule.append(True)

        ev: Event
        for ev in events:
            self.scheduleEvent(ev)
            print(ev.name + " added!")

    # tries to schedule event in correct place, return true if successful, else false and does nothing
    def scheduleEvent(self, ev) -> bool:
        startTime = ev.startTime
        duration = ev.duration
        index = startTime // self.interval  # the start time of the event within our interval

        # for future, check error handling for when the event goes over the time
        # the GUARD to check if everything in the schedule is empty
        if self.checkIfAvailable(startTime, duration):
            # actually setting the events in the schedule, assuming that it is empty
            for i in range(index, index + duration // self.interval):
                self.schedule = ev
            return True
        else:
            return False

    # checking if all the times in the schedule are True, aka nothing scheduled
    def checkIfAvailable(self, startTime, duration) -> bool:
        index = startTime // self.interval  # the start time of the event within our interval
        empty = True
        for i in range(index, index + duration // self.interval):
            if type(self.schedule[i]) == bool:
                empty = empty and self.schedule
            else:
                empty = False
                break
        return empty

    def getNumEvents(self) -> int:
        return len(self.events)

    def printSchedule(self):
        stringV = ""
        for i in range(len(self.schedule)):
            if type(self.schedule[i]) == bool:
                stringV = stringV + "," + toString(self.schedule[i])
            else:
                stringV = stringV + "," + self.schedule[i].name

        return stringV


