import appointment
from enum import Enum
import datetime
import calendar


'''
    The Days and Hours class may not be necessary.  I have found a module
    that does date and time like the server will probably do it
'''
class Days(Enum):
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5

class Hours(Enum):
    eight = 1
    nine = 2
    ten = 3
    eleven = 4
    twelve = 5 
    one = 6
    two = 7
    three = 8 
    four = 9
    five = 10

class tutorSched():
    
    def __init__(self, newCourse, newHours):
        self.course = newCourse
        
        days = {name: i for i, name in enumerate(calendar.day_name)}
        days.pop("Saturday")
        days.pop("Sunday")
        
        self.days = days
        self.hours = newHours


