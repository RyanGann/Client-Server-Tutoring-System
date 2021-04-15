import json

import student


class Appointment():
    appointment = {}
    appointment['appointment'] = []
    
    '''
    def __init__(self, newDate, newTut, newStud, newCrs, newCompl):
        self.datetime = newDate
        self.tutor = newTut
        self.student = newStud
        self.course = newCrs
        self.completed = newCompl
    '''
    def __init__(self, newDateTime, newTut, newCourse, newCompl):
        self.dateTime = newDateTime
        self.tutor = newTut
        self.course = newCourse
        self.completed = newCompl

    def addAppointment(self):
        #Load from file
        with open('appointments.json') as appointments:
            appointment = json.load(appointments)

        
        #add appointment data
        appointment['appointment'].append({
            'dateTime': self.dateTime,
            'tutor': self.tutor,
            'course': self.course,
            'completed': self.completed
        })

        # write back to the JSON file
        with open('appointments.json', 'w') as appointments:
            json.dump(appointment, appointments)