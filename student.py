#list of commands

import json
import sys
import os
import smtplib, ssl

from appointment import Appointment


def studentloop(user, password):   #note change this name maybe
    cmd = ""
    while cmd != "exit":
    
        #version1.clear_screen()     #do we want to use this?

        cmd = (input('> '))
        cmdlist = cmd.split()

        if len(cmdlist) == 3 and cmdlist[0] == "regact":
            regact(cmdlist[1], cmdlist[2])
            
        elif len(cmdlist) == 1 and cmdlist[0] == "edact":
            edact()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "vtut":
            vtut()
            
        elif len(cmdlist) == 5 and cmdlist[0] == "aapt":
            aapt(cmdlist[1], cmdlist[2], cmdlist[3], cmdlist[4])
            
        elif len(cmdlist) == 4 and cmdlist[0] == "edapt":
            edapt(cmdlist[1], cmdlist[2], cmdlist[3])
            
        elif len(cmdlist) == 4 and cmdlist[0] == "dapt":
            dapt(cmdlist[1], cmdlist[2], cmdlist[3])
            
        elif len(cmdlist) == 1 and cmdlist[0] == "emcon":
            emcon()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "emrem":
            emrem()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "psr":   #note some of these might actually need more params
            psr()
            
        elif len(cmdlist) == 1 and cmdlist[0] == "help":  #do we want it to be --help or just help
            gethelp()
            
        elif cmd != "exit":
            print("invalid command")

     # should maybe make it specificy if the command is invalid because
     # the number of params is incorrect or if its invalid because
     # that command just doesnt exist


#below are all the student function definitions:

def regact(email, password):
    acct = {}
    acct['user'] = []
    acct['user'].append({
        'email': email,
        'password': password
    })

    with open('accounts.json', 'w') as accounts:
        json.dump(acct, accounts)

    print("-- account registered --")

def edact():
    print("edit account")

def vtut():
    print("view tutors")

def aapt(dateTime, tutor, course, compl):
    newApt = Appointment(dateTime, tutor, course, compl)
    newApt.addAppointment()
    print("Appointment has been added and scheduled")

def edapt(dateTime, tutor, course):
    with open('appointments.json') as f:
        data = json.load(f)

    edit = " "
    for item in data['appointment']:
        if (dateTime == item['dateTime'] and
            tutor == item['tutor'] and
            course == item['course']):
            while(edit != "nevermind"):
                edit = input("What would you like to edit?(dateTime, tutor, course, completed, or nevermind)")
                if edit == "dateTime":
                    newDate = input("New dateTime: ")
                    item['dateTime'] = item['dateTime'].replace(item['dateTime'], newDate)
                    with open('appointments.json', 'w') as f:
                        json.dump(data, f)
                elif edit == "tutor":
                    newTutor = input("New tutor: ")
                    item['tutor'] = item['tutor'].replace(item['tutor'], newTutor)
                    with open('appointments.json', 'w') as f:
                        json.dump(data, f)
                elif edit == "course":
                    newCourse = input("New course: ")
                    item['course'] = item['course'].replace(item['course'], newCourse)
                    with open('appointments.json', 'w') as f:
                        json.dump(data, f)

            print("Appointment eddited successfully!")


def dapt(dateTime, tutor, course):
    json_lines = []
    with open("appointments.json", 'r') as f:
        for line in f.readlines():
            j = json.loads(line)
            if (dateTime != j['dateTime'] and
            tutor != j['tutor'] and
            course != j['course']):
                json_lines.append(line)

    with open("appointments.json", 'w') as f:
        f.writelines('\n'.join(json_lines))


def emcon(email):
    port = 465
    smtp_server = "smtp.gmail.com"
    sender_email = input("Type your gmail: ")
    receiver_email = email
    password = input("Type the password to your email address: ")
    message = """\
    Subject: Hi there

    This is a test email confirmation."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

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



              
if __name__ == "__main__":
    email = input("Enter an email: ")
    password = input("Create a password: ")

    registerAcct(email, password)
