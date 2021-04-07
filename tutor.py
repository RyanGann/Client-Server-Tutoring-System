from user import User

class Tutor(User):

    def __init__(self, newEmail, newName, newPswrd):
        self.email = newEmail
        self.name = newName
        self.password = newPswrd
        #self.aptSched =  

    def papt():
        print("Get all current appointments from server")

    def capt():
        print("Complete an appointment by the key")

    '''
    Date/time key
    '''
    def aapt():
        print("Create new appointment.  Need a date, student, and course number")

    def edapt():
        print("Edit appointment with new date, student, or course number")

    def dapt():
        print("Delete an appointment by given date, student, and course number")


myTutor = Tutor("hbrown7@una.edu", "Houston Brown", "password")
myTutor.pswrdReset()
