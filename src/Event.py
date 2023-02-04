class Event:
    startTime = 0
    duration = 0
    endTime = 0
    name = ""
    description = ""

    # Create an event starting at startTime minutes from midnight, that is duration minutes long
    def __init__(self, name, description, startTime, duration) -> None:
        self.startTime = startTime
        self.duration = duration
        self.endTime = duration + startTime
        self.name = name
        self.description = description

    
    def __str__(self) -> str:
        retStr = self.name +  "\n" + self.description

    def to24Time(self) -> str:
        return self.duration // 60 + " : " + self.duration % 60
        

