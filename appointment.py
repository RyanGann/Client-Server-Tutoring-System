import student
import tutor

class Appointment():
    
    def __init__(self, newDate, newTut, newStud, newCrs, newCompl):
        self.datetime = newDate
        self.tutor = newTut
        self.student = newStud
        self.course = newCrs
        self.completed = newCompl