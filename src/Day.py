import Event
class Day:
    events = []
    tasks = []
    schedule = []
    interval = 15  # how many minutes each index in an array takes

    # Require: events is a list of events
    #           tasks are a list of tasks
    def __int__(self, events, tasks):
        self.events = events
        self.tasks = tasks

        # creating the
        for i in range(1140 // self.interval):
            self.schedule.add(True)

        ev: Event
        for ev in events:
            self.scheduleEvent(ev)

    def scheduleEvent(self, ev):
        startTime = ev.startTime
        duration = ev.duration
        successful = True

        index = startTime // self.interval  # the start time of the event within our interval

        # This for loop adds the events to the schedule at the correct time
        # TODO: for future, check error handling for when the event goes over the time
        for i in range(index, index + duration // self.interval):
            if type(self.schedule[i]) == bool and self.schedule[i]:
                self.schedule[i] = ev
            else:
                successful = False

        return successful





    def getNumEvents(self):
        return len(self.events)


