'''
  Driver file for CS455 Client/Tutor Scheduling System

  04/26/2021
'''
import json
import requests
import getpass

from requests.exceptions import HTTPError
from tutor import tutorloop
from utilities import clear_screen

'''
Help page for dashboard
'''
def getHelp():
  print('\nEnter \'login\' to login')
  print('Enter \'regact -u <portal_email>\' to register an account')
  print('Enter \'exit\' to quit')
  print('Enter \'clear\' to clear the screen\n')


def login():
    while True:
        email = ''
        pswrd = ''
        try:
            email = input('\nUsername> ')
            pswrd = getpass.getpass(prompt = 'Password> ')
        except KeyboardInterrupt as kybrd:
            break
        authorize(email, pswrd)
        break


def authorize(email, pswrd):
    try:
        usr_name = email.split("@")[0]
        url = 'https://quanthu.life/tutorapp/users/login'
        data = {'username': usr_name,
                'password': pswrd}
        print(data)
        x = requests.post(url, json = data)
        response = json.loads(x.text)
        print(response["message"])
        if response["message"] == 'Login successfully.':
            print(response['data']['role'])
        if response['data']['role'] == "TUTOR":
           tutorloop(usr_name, pswrd)

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
    except Exception as err:
        print(f'Error: {err}')


def temp_login():
   email = 'rgann2@una.edu'
   pswrd = 'Ham1234'

   try:
      url = 'https://quanthu.life/tutorapp/users/role/student'
      x = requests.get(url)
      resp = json.loads(x.text)
      role = ''
      for users in resp['data']:
         if email == users['email'] and pswrd == users['password']:
            role = users['role']
      if role == 'STUDENT':
         clear_screen()
         studentloop(email)
      elif role == 'admin':
         adminloop(email)
      elif role == 'tutor':
         tutorloop(email)
      
   except HTTPError as http_err:
      print(f'HTTP error occured: {http_err}')
   except Exception as err:
      print(f'Error: {err}')



if __name__ == '__main__':
   
   clear_screen()
   print('********************************************************************************')
   print('*                        University of North Alabama                           *')
   print('*                    Tutor Appointment Management System                       *')
   print('*                                                                              *')
   print('*  For help enter --help                                                       *')
   print('********************************************************************************')

   cmd = ''
   while cmd != 'exit':
      try:
         cmd = (input('UNA> '))
         cmdList = cmd.split()
      
         if cmdList[0] == '--help':
            getHelp()

         elif cmdList[0] == 'login':
            login()

         elif cmdList[0] == 'regact':
            reg(cmd, cmdList)
               
         elif cmdList[0] == 'exit':
            clear_screen()
            exit

         elif cmdList[0] == 'clear':
            clear_screen()
        
         else:
            print('Error: Invalid command')
             
      except KeyboardInterrupt as e:
         cmd = 'exit'
      except IndexError as ind:
         print(f'Error: Please try again')
         continue
      except Exception as ex:
         print(f'Error: Please try again')
         continue
