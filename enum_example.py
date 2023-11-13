from enum import Enum
class Weekday(Enum):
    sunday = 1
    monday = 2
    tuesday = 3
    wednesday = 4
    thursday = 5
    friday = 6
    saturday = 7
def checkday(value):

    result : str = ""
    match(value):
        case Weekday.monday.value:
            result = "weekday"
        case Weekday.tuesday.value:
            result = "tuesday"
        case Weekday.wednesday.value:
            result = "weekday"
        case Weekday.thursday.value:
            result = "weekday"
        case Weekday.friday.value:
            result = "Weekday"
        case  Weekday.saturday.value:
            result = "Weekend"
        case Weekday.sunday.value:
            result = "Weekend"
    return result
day = int(input("enter a value : "))
print(checkday(day))
print(type(Weekday))
print(Weekday.saturday)
print(Weekday.sunday)
print(Weekday.thursday.name)



