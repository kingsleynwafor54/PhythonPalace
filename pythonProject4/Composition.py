import enum


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def getAge(self):
        return self.age

    def getName(self):
       return self.name

    def setName(self, name):
        self.name=name;

    def setAge(self,age):
        self.age=age



d= Animal("django",12)
print(d.getAge())


class Days(enum.Enum):
    mon="Monday"
    tue="Tuesday"
    wed="Wednessday"
    thur="Thursday"
    def getMon(self):
        return self.mon


for weekly in Days:
    print(weekly.value)