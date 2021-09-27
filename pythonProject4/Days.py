import enum


class Days(enum.Enum):
    mon="Monday"
    tue="Tuesday"
    wed="Wednessday"
    thur="Thursday"
    def getMon(self):
        return self.mon


for weekly in Days:
    print(weekly.value)