import getpass
import requests
from requests.exceptions import HTTPError
import json
from utilities import clear_screen
from utilities import psr

def student_loop(usr):
    cmd = ''
    
    while cmd != 'logout':
    
        try:
            cmd = (input(f'{usr}> '))
            cmdlist = cmd.split()
                
            if len(cmdlist) == 5 and cmdlist[0] == 'edact':
                edact(usr, cmdlist)
                
            elif len(cmdlist) == 1 and cmdlist[0] == 'vtut':
                print()
                vtut()

            elif len(cmdlist) == 9 and cmdlist[0] == 'aapt':
                aapt(cmdlist, usr)
                
            elif cmdlist[0] == 'edapt':   
                edapt(cmdlist)
                
            elif cmdlist[0] == 'dapt':
                dapt(cmdlist)
                
            elif len(cmdlist) == 1 and cmdlist[0] == 'emcon':
                emcon()
                
            elif len(cmdlist) == 1 and cmdlist[0] == 'emrem':
                emrem()
                
            elif len(cmdlist) == 1 and cmdlist[0] == 'psr': 
                psr(usr)
                
            elif len(cmdlist) == 1 and cmdlist[0] == '--help':  
                gethelp()

            elif len(cmdlist) == 1 and cmdlist[0] == 'clear':
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
        
    
# edact -u new -p new
def edact(usr, cmdlist):
    url = 'https://quanthu.life/tutorapp/users'
    usrs = requests.get(url)
    usrs_resp = json.loads(usrs.text)
    
    data = {}
    is_found, _id = True, ''

    if cmdlist[1] == '-u' and cmdlist[3] == '-p':
        for item in usrs_resp['data']:
            if usr == item['username']:
                _id = item['_id']
                
                data = {'_id': item['_id'],
                        'username': cmdlist[2],
                        'email': item['email'],
                        'password': item['password'],
                        'phone': cmdlist[4],
                        'role': item['role'],
                        'lastActivityDateTime': item['lastActivityDateTime'],
                        'isActive': item['isActive']
                    }
                is_found = True
                url = url + "/" + _id
                put_req = requests.put(url, json = data)
                resp = json.loads(put_req.text)
                if resp['errorCode'] == 200:
                    print('Your account has been successfully edited')
                else:
                    print('Your account was not edited successfully') 
                break
            else: is_found = False
            

        #update username

    else:
        print('Error: Wrong argument passed')
    

def vtut():
    url = 'https://quanthu.life/tutorapp/schedule'

    x = requests.get(url)
    resp = json.loads(x.text)
        
    col_width = 0
    for users in resp['data']:
        if col_width < len(users['tutor_id']):
            col_width = len(users['tutor_id'])
                
    print('\tTutor ID', '%20s'%'Date', '%20s'%'Start Time', '%15s'%'End Time')
    print('==============================================================='\
                '===============')

    for users in resp['data']:
        print(users['tutor_id'],
            '%30s'% users['weekday'],
            '%15s'% users['from_time'].center(5),
            '%15s' %users['end_time'].center(5))
    print()



def aapt(cmdlist, usr):
    url = 'https://quanthu.life/tutorapp/appointment'

    if cmdlist[1] == '-t' and cmdlist[3] == '-d' and cmdlist[5] == '-f' \
       and cmdlist[7] == '-e':
        
        # First validate the tutor username that was passed
        tutor_id = str(cmdlist[2])
        tutor_url = 'http://quanthu.life:8000/users/role/TUTOR'
        is_found = False
        
        tutor_req = requests.get(tutor_url)
        tutors = json.loads(tutor_req.text)

        # Loop through the list of tutors if request is successful
        if tutors['errorCode'] == 200:
            for tutor in tutors['data']:
                if tutor_id == tutor['username']:
                    is_found = True
        else:
            print(tutors['errorCode'])

        if is_found == True:
            new_date = str(cmdlist[4])
            from_time = str(cmdlist[6])
            end_time = str(cmdlist[8])

            data = {'tutor_id': tutor_id,
                    'student_id': usr,
                    'date': new_date,
                    'from_time': from_time,
                    'end_time': end_time,
                    'isCompleted': False,
                    'isActive': True
                    }

            req = requests.post(url, json = data)
            resp = json.loads(req.text)

            if resp['errorCode'] == 200:
                print('New appointment has been scheduled')
            else:
                print(resp['errorCode'])
        else:
            print('Invalid tutor username')

    else:
        print('Error: Invalid argument(s)')



def edapt(cmdlist):
    if cmdlist[1] == '-t' and cmdlist[3] == '-d' and cmdlist[5] == '-f' \
       and cmdlist[7] == '-e':
        
        newTut = str(cmdlist[2])
        url = 'https://quanthu.life/tutorapp/users/role/TUTOR'
        is_found = True
        
        tut_req = requests.get(url)
        tuts = json.loads(tut_req.text)

        for item in tuts['data']:
            if newTut == item['username']:
                tut_usr = item['username']
                is_found = True
                break
                
            else: is_found = False

        if is_found == False:
            print('Invalid Tutor ID')
            
        else:
            apt_url = 'https://quanthu.life/tutorapp/appointment'
            apt_req = requests.get(apt_url)
            apt_resp = json.loads(apt_req.text)
            
            for item in apt_resp['data']:
                if newTut == item['tutor_id']:
                    _id = item['_id']
                    put_url = apt_url + "/" +  _id
                    data = {"_id": item["_id"],
                            "tutor_id": newTut,
                            "student_id": item['student_id'],
                            "date": cmdlist[4],
                            "from_time": cmdlist[6],
                            "end_time": cmdlist[8],
                            "isCompleted": False,
                            "isActive": True}
                    
                    put_req = requests.put(put_url, json = data)
                    put_resp = json.loads(put_req.text)
                    print(put_resp['message'])
                else:
                    print('Tutor not found')

        

def dapt(cmdlist):
    _id = input("Enter the id of the appointment you would like to delete: ")

    url = 'http://quanthu.life:8000/appointment/' + _id
    response = requests.delete(url)
    
    if response.status_code == 200:
        print("Successfully deleted selected appointment")
    elif response.status_code == 404:
        print("Unsuccessful request")

def emcon():
    print("Waiting on server...\n")
    
def emrem():
    print("Waiting on server...\n")
    
def gethelp():
    infile = open("help_student.txt", "r")
    lines = infile.readlines()

    for line in lines:
        print(line, end = "")
	
    print()
    infile.close()

