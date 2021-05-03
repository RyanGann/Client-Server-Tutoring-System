import requests
from requests.exceptions import HTTPError
import json
#from utilities import clear_screen


def admin_loop(usr):
    name = usr.split('@')[0]
    cmd = ''

    while cmd != 'logout':
        try:
            cmd = (input(f'{name}> '))
            cmd_list = cmd.split()

            if cmd_list[0] == 'adad':
                adad()

            elif cmd_list[0] == 'edad':
                edad()

            elif cmd_list[0] == 'delad':
                delad()

            elif cmd_list[0] == 'adfac':
                adfac()

            elif cmd_list[0] == 'edfac':
                edfac()


            elif cmd_list[0] == 'delfac':
                delfac()


            elif cmd_list[0] == 'adtut':
                adtut()

            elif cmd_list[0] == 'edtut':
                edtut()

            elif cmd_list[0] == 'deltut':
                deltut()

            elif cmd_list[0] == 'adts':
                adts()

            elif cmd_list[0] == 'edts':
                edts()
                
            elif cmd_list[0] == 'delts':
                delts()

            elif cmd_list[0] == 'psa':
                psa()

            elif cmd_list[0] == 'papt':
                papt()

            elif cmd_list[0] == 'rnrpt':
                rnrpt()

            elif cmd_list[0] == 'srpt':
                srpt()

            elif len(cmd_list) == 1 and cmd_list[0] == '--help':  #do we want it to be --help or just help
                gethelp()

            elif len(cmd_list) == 1 and cmd_list[0] == 'clear':
                clear_screen()
                
            elif cmd != 'logout':
                print('Error: Invalid command')

        except IndexError as ind:
            print('Error: Wrong number of arguements')
            continue
        except HTTPError as http_err:
            print(f'HTTP Error occured: {http_err}')
            continue
        except KeyboardInterrupt as kybrd:
            cmd = 'logout'
            continue
        except Exception as err:
            print(f'Error: {err}')
            continue


def adad():
    response = requests.get('http://quanthu.life:8000/users')
    if response.status_code == 200:
        print("Successfully retrieved information")
    elif response.status_code == 404:
        print("Failed to retrieve information")

    usrnme = input("Create a username: ")
    email = input("Enter an email address: ")
    psswrd = input("Create a password: ")
    phone = input("Enter your phone number: ")
    
    data = {
        "username": usrnme,
        "email": email,
        "password": psswrd,
        "phone": phone,
        "role": "admin",
        "isActive": True
    }

    posts = requests.post('http://quanthu.life:8000/users', json = data)

def edad():
    id = input("Enter the id of the admin you would like to edit: ")

    usrnme = input("Create a username: ")
    email = input("Enter an email address: ")
    psswrd = input("Create a password: ")
    phone = input("Enter your phone number: ")
    
    data = {
        "username": usrnme,
        "email": email,
        "password": psswrd,
        "phone": phone,
        "role": "admin",
        "isActive": True
    }

    url = 'http://quanthu.life:8000/users/' + id

    posts = requests.put(url, json = data)

def delad():
    id = input("Enter the id of the admin you would like to delete: ")

    url = 'http://quanthu.life:8000/users/' + id

    posts = requests.delete(url, data = "deleting admin")

def adfac():
    print("Add a new faculty account")

def edfac():
    print("Edit a faculty's email, name, or password")

def delfac():
    print("Delete a faculty's account by email")

def adtut():
    print("Add a new Tutor account")

def edtut():
    print("Edit a tutor's email, name, or password")

def deltut():
    print("Delete a tutor's account by email")

def adts():
    print("Add a new schedule object to a given tutor")

def edts():
    print("Change a given tutor's availability schedule")

def delts():
    print("Delete a given tutor's availability schedule")

def psa():
    print("Purge a student account by email")

def papt():
    print("Purge an appointment by given date")

def rnrpt():
    print("Run a given report")

def srpt():
    print("Schedule a report to be emailed periodically")

def gethelp():
    infile = open("help_admin.txt", "r")

    lines = infile.readlines()

    for line in lines:
        print(line, end = "")

    print()
	    
    infile.close()

if __name__ == '__main__':
    admin_loop('hbrown7@una.edu')
