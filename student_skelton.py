#list of commands

# this just has the function names which are yet to be filled in
# note the name of this file is student_skeleton.py not student.py which means it wont work
# with the current version1.py program cause that one imports student not student_skeleton


import os
#import version1

def stuff():   #note change this name
    cmd = ""
    while cmd != "exit":
        #version1.clear_screen()
        cmd = (input('> '))
        if cmd == "regact":
            regact()
        elif cmd == "edact":   #this was not on overleaf doc
            editacct()
        elif cmd == "vtut":
            vtut()
        elif cmd == "aapt":
            aapt()
        elif cmd == "edapt":
            edapt()
        elif cmd == "dapt":
            dapt()
        elif cmd == "emcon":
            emcon()
        elif cmd == "emrem":
            emrem()
        elif cmd == "psr":
            psr()
        elif cmd == "--help":
            gethelp()
        elif cmd != "exit":
            print("invalid command")



def regact():
    print("register account")

def edact():
    print("edit account")

def vtut():
    print("view tutors")

def aapt():
    print("Appointment has been added and scheduled")

def edapt():
    print("edit appointment")

def dapt():
    print("delete appointment")

def emcon():
    print("email confirmation")

def emrem():
    print("email reminder")

def psr():
    print("Password has been reset")
    
def gethelp():
    print("regact\tRegister account with given email and password\n")
    print("edact\tEdit account details\n")
    print("vtut\tView list of tutors by given date and course number\n")
    print("aapt\tAdd appointment by a given date, tutor, and course number\n")
    print("edapt\tEdit current appointment with new date, tutor, or course number\n")
    print("dapt\tDelete appointment by a given date, tutor, and course number\n")
    print("emcon\tSend an email confirmation of appointment to student email provided a given date\n")
    print("emrem\tSend an email reminder of appointmentto student email provided a given date\n")
    print("psr\tPassword reset that takes old and then new password\n")
