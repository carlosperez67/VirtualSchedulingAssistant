from Event import Event
from Day import Day

# SETUP
testEvent = Event("ALIFHHFH", "start at 10am!!", 600, 60)
testEvents = [testEvent]
testTasks = [1]

testDay = Day(testEvents, testTasks)

print(testDay.printSchedule())
