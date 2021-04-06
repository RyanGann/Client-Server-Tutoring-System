#list of commands

# this just has the function names which are yet to be filled in
# note the name of this file is student_skeleton.py not student.py which means it wont work
# with the current version1.py program cause that one imports student not student_skeleton

import sys
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
