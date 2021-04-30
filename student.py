import getpass
import requests
from requests.exceptions import HTTPError
import json
from utilities import clear_screen

def studentloop(usr):   #note change this name maybe
    name = usr.split("@")[0]
    cmd = ""
    
    while cmd != "logout":
    
        try:
            cmd = (input(f'{name}> '))
            cmdlist = cmd.split()
                
            if len(cmdlist) == 1 and cmdlist[0] == "edact":
                edact()
                
            elif len(cmdlist) == 1 and cmdlist[0] == "vtut":
                print()
                vtut()
                
            elif cmdlist[0] == "aapt":
                aapt(cmdlist)
                
            elif cmdlist[0] == "edapt":   
                edapt(cmdlist)
                
            elif cmdlist[0] == "dapt":
                dapt(cmdlist)
                
            elif len(cmdlist) == 1 and cmdlist[0] == "emcon":
                emcon()
                
            elif len(cmdlist) == 1 and cmdlist[0] == "emrem":
                emrem()
                
            elif len(cmdlist) == 1 and cmdlist[0] == "psr":   #note some of these might actually need more params
                curStudent.pswrdReset()
                
            elif len(cmdlist) == 1 and cmdlist[0] == "--help":  #do we want it to be --help or just help
                gethelp()

            elif len(cmdlist) == 1 and cmdlist[0] == "clear":
                clear_screen()
                
            elif cmd != "logout":
                print("Error: Invalid command")

        except IndexError as ind:
            print("Error: Wrong number of arguements")
            continue
        except HTTPError as http_err:
            print(f'HTTP Error occured: {http_err}')
            continue
        except KeyboardInterrupt as kybrd:
            cmd = "logout"
            continue
        except Exception as err:
            print(f'Error: {err}')
            continue


#below are all the student function definitions:
    

def edact(cmdlist):
    print("edit account")
    

def vtut():
    try:
        url = 'https://quanthu.life/tutorapp/schedule'

        x = requests.get(url)
        resp = json.loads(x.text)
        
        col_width = 0
        for users in resp['data']:
            if col_width < len(users['tutor_id']):
                col_width = len(users['tutor_id'])
                
        print('Tutor ID', '%13s'%'Date', '%17s'%'Start Time', '%15s'%'End Time')
        print('=========================================================')

        for users in resp['data']:
            print(users['tutor_id'].center(col_width),
                  '%15s'% users['date'].ljust(col_width),
                  '%15s'% users['from_time'].center(col_width),
                  '%15s' %users['end_time'].center(col_width))
            
    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Error: {err}')    




'''
-t Tutor
-c Course
-d Date
-s Time
'''
# aapt -t Jalen Jones -c CS355 -d 4/16/2021 -t 1200
def aapt(cmdlist):
    infile = open("appointments.txt", "a")

    if len(cmdlist) < 10:
        print("Error: wrong number of arguements")
        
    elif cmdlist[4] == '-c':
        tutor = cmdlist[2] + " " + cmdlist[3]
        subj = cmdlist[5]
        date = cmdlist[7]
        time = cmdlist[9]
        infile.write(tutor + " " + subj + " "  + date + " " + time + "\n")
        
    else:
        print("Error: invalid arguement placement")
    
    infile.close()
    print("Appointment has been added and scheduled")


def edapt(cmdlist):
    infile = open("appointments.txt", "a")

    if len(cmdlist) < 10:
        print("Error: wrong number of arguements")
    elif cmdlist[4] == '-c':
        name = cmdlist[2] + " " + cmdlist[3]
        course = cmdlist[5]
        day = cmdlist[7]
        time = cmdlist[9]
        infile.write(name + " " + course + " "  + day + " " + time + "\n")
    else:
        print("Error: invalid arguement placement")
    
    infile.close()    
    print("Appointment has been edited")

# dapt -t Jalen Jones -c CS355 -d 4/16/2021 -t 1200
def dapt(cmdlist):
    ctr = 0
    infile = open("appointments.txt", "r")
    
    if len(cmdlist) < 10:
        print("Error: wrong number of arguements")
    elif cmdlist[4] == '-c':
        lines = infile.readlines()
        infile.close()

        command = cmdlist[2] + " " + cmdlist[3] + " " + cmdlist[5] + " " +\
                  cmdlist[7] + " " + cmdlist[9]

        for line in lines:
            if line[ctr] == command[ctr]:
                print()
                #Deletion command goes here
            ctr = ctr + 1

        infile = open("appointments.txt", "w+")

        for line in lines:
            infile.write(line)
    else:
        print("Error: invalid arguement placement")
            
    infile.close()
    print("Appointment has been deleted")


def emcon():
    print("emial conrimation")
    
def emrem():
    print("email reminder")
    
def gethelp():
	infile = open("help_student.txt", "r")

	lines = infile.readlines()

	for line in lines:
		print(line, end = "")

	print()
	    
	infile.close()

if __name__ == '__main__':
    vtut()

