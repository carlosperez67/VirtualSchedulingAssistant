class Day:
    events = None
    schedule = []
    interval = 15  # how many minutes each index in an array takes

    def __int__(self, events):
        self.events = events

        for i in range(int(1140 / self.interval)):
            self.schedule.add(True)


    def getNumEvents(self):
        return len(self.events)

    def

