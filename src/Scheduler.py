from Day import Day


class Scheduler:

    def schedule(self, day: Day) -> Day:
        toSchedule = day.tasks
        schedule = day.schedule
        interval = day.interval
        for task in toSchedule:
            try:
                while (task.unscheduled > 0):
                    index = toSchedule.index(True)
                    duration = interval
                    startTime = index * interval
                    i = index + 1
                    while (type(schedule[i]) == bool and schedule[i]):

                        duration += interval
                        pass

            except:
                print("Schedule full")

        return day
