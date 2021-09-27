import enum


class Days(enum.Enum):
    MONDAY = "Monday"
    TUESDAY= "Tuesday"
    WEDNESDAY = "Wednessday"
    THURSDAY = "Thursday"
    def getMon(self):
        return self.mon


for weekly in Days:
    print(weekly.value)