import requests
from requests.exceptions import HTTPError
import json
from utilities import clear_screen
from utilities import psr

def fac_loop(usr):
    cmd = ''

    while cmd != 'logout':
        try:
            cmd = (input(f'{usr}> '))
            cmd_list = cmd.split()

            if len(cmd_list) == 2 and cmd_list[0] == 'rnrpt':
                rnrpt(cmd_list)

            elif len(cmd_list) == 1 and cmd_list[0] == 'srpt':
                srpt()

            elif len(cmd_list) == 1 and cmd_list[0] == 'psr':
                psr(usr)

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

'''
rnrpt -l: List of tutors and their availability schedules
rnrpt -p: Student activity by date range and course(scheduled and completed)
rnrpt -r: Tutor activity by date range and course (scheduled and completed)
'''
def rnrpt(cmd_list):
    if cmd_list[1] == '-l':
        print('List of tutors and their availability schedules\n')

    elif cmd_list == '-p':
        print('Student activity by date range and course(scheduled and completed)\n')

    elif cmd_list == '-r':
        print('Tutor activity by date range and course (scheduled and completed)\n')

    else:
        print('Error: Invalid argument(s)\n')
    
    

def srpt():
    print("Schedule a report to be emailed periodically\n")

    

def gethelp():
        infile = open("help_faculty.txt", "r")
        lines = infile.readlines()

        for line in lines:
            print(line, end = "")

        print()   
        infile.close()
