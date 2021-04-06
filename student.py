#list of commands

import sys
import os

import json


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
