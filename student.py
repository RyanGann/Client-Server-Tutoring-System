#list of commands

import json
import sys
import os
import smtplib, ssl

def registerAcct(email, password):
    acct = {}
    acct['user'] = []
    acct['user'].append({
        'email': email,
        'password': password
    })

    with open('accounts.txt', 'w') as accounts:
        json.dump(acct, accounts)


def mkapt(date, subject, tutor):
    data = {}
    data['appointment'] = []
    data['appointment'].append({
        'date': date,
        'subject': subject,
        'tutor': tutor
    })

    with open('newApt.txt', 'w') as outfile:
        json.dump(data, outfile)
        
    print("Appointment has been made and scheduled")

def resetpswrd():
    print("Password has been reset")

def addAppointment ():
    print("")

def emailConfirmation():
    print("")
              
if __name__ == "__main__":
    email = input("Enter an email: ")
    password = input("Create a password: ")

    registerAcct(email, password)
