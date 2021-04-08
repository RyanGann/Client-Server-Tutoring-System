# this just has the function names which are yet to be filled in
# note the name of this file is student_skeleton.py not student.py which means it wont work
# with the current version1.py program cause that one imports student not student_skeleton
# and so it needs to be renamed to student.py in order to be tested


#import os
#import version1

def studentloop():   #note change this name maybe
    cmd = ""
    while cmd != "exit":
    
        #version1.clear_screen()     #do we want to use this?

        cmd = (input('> '))
        cmdlist = cmd.split()

        if len(cmdlist) == 3 and cmdlist[0] == "regact":
            regact(cmdlist[1], cmdlist[2])
            
        elif len(cmdlist) == 1 and cmdlist[0] == "edact":
            editacct()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "vtut":
            vtut()
            
        elif len(cmdlist) == 5 and cmdlist[0] == "aapt":
            aapt(cmdlist[1], cmdlist[2], cmdlist[3], cmdlist[4])
            
        elif len(cmdlist) == 1 and cmdlist[0] == "edapt":
            edapt()
            
        elif len(cmdlist) == 5 and cmdlist[0] == "dapt":
            dapt(cmdlist[1], cmdlist[2], cmdlist[3], cmdlist[4])
            
        elif len(cmdlist) == 1 and cmdlist[0] == "emcon":
            emcon()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "emrem":
            emrem()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "psr":   #note some of these might actually need more params
            psr()
            
        elif len(cmdlist) == 4 and cmdlist[0] == "--help":  #do we want it to be --help or just help
            gethelp()
            
        elif cmd != "exit":
            print("invalid command")

     # should maybe make it specificy if the command is invalid because
     # the number of params is incorrect or if its invalid because
     # that command just doesnt exist


#below are all the student function definitions:

def regact(email, password):
    print("register account")

def edact():
    print("edit account")

def vtut():
    print("view tutors")

def aapt(tutor, subj, date, time):
    print("Appointment has been added and scheduled")

def edapt():
    print("edit appointment")

def dapt(tutor, subj, date, time):
    print("delete appointment")

def emcon():
    print("email confirmation")

def emrem():
    print("email reminder")

def psr():
    print("Password has been reset")
    
def gethelp():
    print("regact\tRegister account with given email and password\n")
    print("edact\tEdit account details (name, phone number)\n")
    print("vtut\tView list of tutors by given date and course number\n")
    print("aapt\tAdd appointment by a given date, tutor, and course number\n")
    print("edapt\tEdit current appointment with new date, tutor, or course number\n")
    print("dapt\tDelete appointment by a given date, tutor, and course number\n")
    print("emcon\tSend an email confirmation of appointment to student email provided a given date\n")
    print("emrem\tSend an email reminder of appointmentto student email provided a given date\n")
    print("psr\tPassword reset that takes old and then new password\n")
