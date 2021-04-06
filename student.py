#list of commands


import sys
import os
#import version1

def stuff():   #note change this name
    cmd = ""
    while cmd != "exit":
        cmd = (input('> '))
        #version1.clear_screen()
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
        else:
            print("invalid command")



def regact():
    print("register account")

def edact():
    print("edit account")

def viewtutors():
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
