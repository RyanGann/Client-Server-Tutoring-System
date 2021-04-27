from user import User
from appointment import Appointment

class Tutor():


    def tutorloop(self, user, password):
        print("Tutor Loop")

    def __init__(self, newEmail, newName, newPswrd):
        self.email = newEmail
        self.name = newName
        self.password = newPswrd
        self.Appointments = []

    def papt():
        print("Get all current appointments from server")

    def capt():
        print("Complete an appointment by the key")

    '''
    Date/time key
    '''
    def aapt():
        file1 = open("appointment.txt", "a")
        date = input("Enter date: ")
        student = input("Enter student: ")
        course = input("Enter course: ")
        L = [date, student, course]
        file1.writelines(L)
        file1.close()
        #print("Create new appointment.  Need a date, student, and course number")

    def edapt():
        print("Edit appointment with new date, student, or course number")

    def dapt():
        print("Delete an appointment by given date, student, and course number")
        
    def gethelp():
        print("papt\tView all current appointments\n")
        print("capt\tComplete given appointment\n")
        print("aapt\tAdd appointment by a given date, student, and course number\n")
        print("edapt\tEdit current appointment with new date, student, or course number\n")
        print("dapt\tDelete appointment by given date, student, and course number\n")
        print("psr\tPassword reset that takes old and then new password\n")

