import requests
from requests.exceptions import HTTPError
import json
from utilities import clear_screen
from utilities import psr


def admin_loop(usr):
    cmd = ''

    while cmd != 'logout':
        try:
            cmd = (input(f'{usr}> '))
            cmd_list = cmd.split()

            if len(cmd_list) == 3 and cmd_list[0] == 'adad':
                add_account(cmd_list, 'ADMIN')
            
            elif cmd_list[0] == 'edad':
                edad()

            elif len(cmd_list) == 3 and cmd_list[0] == 'delad':
                del_account(cmd_list)

            elif cmd_list[0] == 'adfac':
                add_account(cmd_list, 'FACULTY')

            elif cmd_list[0] == 'edfac':
                edfac()

            elif cmd_list[0] == 'delfac':
                del_account(cmd_list)

            elif cmd_list[0] == 'adtut':
                add_account(cmd_list, 'TUTOR')

            elif cmd_list[0] == 'edtut':
                edtut()

            elif cmd_list[0] == 'deltut':
                del_account(cmd_list)

            elif len(cmd_list) == 9 and cmd_list[0] == 'adts':
                adts(cmd_list)

            elif cmd_list[0] == 'edts':
                edts()
                
            elif cmd_list[0] == 'delts':
                delts()

            elif cmd_list[0] == 'psa':
                psa(cmd_list)

            elif cmd_list[0] == 'papt':
                papt()

            elif cmd_list[0] == 'psr':
                psr(usr)

            elif cmd_list[0] == 'rnrpt':
                rnrpt()

            elif cmd_list[0] == 'srpt':
                srpt()

            elif len(cmd_list) == 1 and cmd_list[0] == '--help':
                gethelp()

            elif len(cmd_list) == 1 and cmd_list[0] == 'clear':
                clear_screen()
                
            elif cmd != 'logout':
                print('Error: Invalid command')
            
        except IndexError as ind:
            if cmd == '\r' or '\n': continue
            else:
                print('Error: Wrong number of arguments')
                continue
        except HTTPError as http_err:
            print(f'HTTP Error: {http_err}')
            continue
        except KeyboardInterrupt as kybrd:
            cmd = 'logout'
            print()
        except Exception as err:
            print(f'Error: {err}')
            continue
            


def add_account(cmd_list, new_role):
    if cmd_list[1] == '-u':
        usr_name = str(cmd_list[2])
        pswrd = 'Leo'
        pswrd = pswrd + usr_name + '!'
        email = usr_name + '@una.edu'

        url = 'https://quanthu.life/tutorapp/users'
        data = {'username': usr_name,
                'email': email,
                'password': pswrd,
                'phone': "",
                'role': new_role
                }
        req = requests.post(url, json = data)
        resp = json.loads(req.text)

        if resp['errorCode'] == 200:
            print('New user has been successfully created')
        elif resp['errorCode'] == 404:
            print(resp['message'])
                
    else:
        print('Error: invalid arguement(s)')



def del_account(cmd_list):
    if cmd_list[1] == '-u':
        is_found = True
        users_url = 'https://quanthu.life/tutorapp/users/'
        
        req = requests.get(users_url)
        users = json.loads(req.text)
        
        if users['errorCode'] == 200:
            for item in users['data']:
                if cmd_list[2] == item['username']:
                    is_found = True
                    _id = item['_id']
                    del_url = users_url + _id
                    del_usr = requests.delete(del_url)
                    del_resp = json.loads(del_usr.text)
                    
                    if del_resp['errorCode'] == 200:
                        print('User has been successfully deleted')
                    else:
                        print(del_resp['message'])
                else: is_found = False

            if is_found == False:
                print('Invalid username')
                        
        elif users['errorCode'] == 404:
          print(users['message'])
    else:
       print('Error: invalid arguement(s)')
        


def edad():
    print("Edit an admin's email, name, or password\n")



def edfac():
    print("Edit a faculty's email, name, or password]n")



def edtut():
    print("Edit a tutor's email, name, or password\n")



#adts -u hbrown5 -d <dateTime> -f <fromTime> -e <endTime>
def adts(cmd_list):
    if cmd_list[1] == '-u' and cmd_list[3] == '-d' and cmd_list[5] == '-f'\
               and cmd_list[7] == '-e':
        is_found  = True
        users_url = 'https://quanthu.life/tutorapp/users'
        sched_url = 'https://quanthu.life/tutorapp/schedule'
        
        req = requests.get(users_url)
        users = json.loads(req.text)

        if users['errorCode'] == 200:
            for item in users['data']:
                if str(cmd_list[2]) == item['username']:
                    is_found = True
                    tutor_id = item['username']
                    data = {'_id': item['_id'],
                            'tutor_id': tutor_id,
                            'weekday': str(cmd_list[4]),
                            'from_time': str(cmd_list[6]),
                            'end_time': str(cmd_list[8]),
                            'isActive': True}
                    
                    sched_req = requests.post(sched_url, json = data)
                    sched_resp = json.loads(sched_req.text)
                    
                    if sched_resp['errorCode'] == 200:
                        print('New schedule has been created')
                    else:
                        print(sched_resp['message'])
                    break
                        
                else: is_found = False
                
            if is_found == False:
                print('Invalid username')
        
        elif users['errorCode'] == 404:
          print(users['message'])
    else:
        print('Error: invalid arguement(s)')

        

def edts():
    print("Change a given tutor's availability schedule\n")



#delts -u hbrown5
#The Deletion server command is not working properly
def delts(cmd_list):
    print("Deleting tutor's schedule\n")



# psa -e hbrown5@una.edu
def psa(cmd_list):
    url = 'https://quanthu.life/tutorapp/users/role/STUDENT'
    is_found = True
    
    if cmd_list[1] == '-e':
        req = requests.get(url)
        students = json.loads(req.text)

        if students['errorCode'] == 200:
            for student in students['data']:
                if cmd_list[2] == student['email']:
                    is_found = True
                    del_id = student['_id']
                    del_url = 'https://quanthu.life/tutorapp/users/' + del_id
                    del_stud = requests.delete(del_url)
                    del_resp = json.loads(del_stud.text)
                
                    if del_resp['errorCode'] == 200:
                        print('User has been successfully deleted')
                    else:
                        print(del_resp['message'])
                        
                else: is_found = False
                
            if is_found == False:
                print('Invalid student account')

        elif students['errorCode'] == 404:
            print(students['errorCode'])

    else:
        print('Error: Invalid argument(s)')

     
  

def papt():
    print("Purge an appointment by given date\n")



def rnrpt():
    if cmd_list == '-a':
        print('List of admins/n')

    elif cmd_list == '-f':
        print('List of faculty members/n')

    elif cmd_list == '-s':
        print('List of distinct students tutored by date range/n')

    elif cmd_list == '-t':
        print('List of tutoring appointments by date range/n')

    elif cmd_list == '-d':
        print('List of distinct students tutored by tutor and date range/n')

    elif cmd_list == '-u':
        print('Total number of hours unused by tutor by date range/n')

    elif cmd_list == '-c':
        print('Total hours available by course by date range/n')

    elif cmd_list[1] == '-l':
        print('List of tutors and their availability schedules/n')

    elif cmd_list == '-p':
        print('Student activity by date range and course(scheduled and completed)/n')

    elif cmd_list == '-r':
        print('Tutor activity by date range and course (scheduled and completed)/n')

    else:
        print('Error: Invalid argument(s)')

def srpt():
    print("Schedule a report to be emailed periodically")

def gethelp():
    infile = open("help_faculty.txt", "r")
    lines = infile.readlines()

    for line in lines:
        print(line, end = "")

    print()   
    infile.close()

