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
            regact('date', 'subject', 'tutor')   # note these are just placeholder parameters
        elif cmd == "edact":                     # this was not on overleaf doc
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

def vtut():
    print("view tutors")

def aapt(date, subject, tutor):
    data = {}
    data['appointment'] = []
    data['appointment'].append({
        'date': date,
        'subject': subject,
        'tutor': tutor
    })

    with open('newApt.txt', 'w') as outfile:
        json.dump(data, outfile)

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
