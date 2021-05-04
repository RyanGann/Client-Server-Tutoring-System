import getpass
import requests
import json
from requests.exceptions import HTTPError
from student import student_loop
from tutor import tutor_loop
from faculty import fac_loop
from admin import admin_loop
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
        usr = ''
        pswrd = ''
        try:
            usr = input('\nUsername> ')
            pswrd = getpass.getpass(prompt = 'Password> ')
        except KeyboardInterrupt as kybrd:
            break
        authorize(usr, pswrd)
        break



def authorize(usr_name, pswrd):
    try:
        url = 'https://quanthu.life/tutorapp/users/login'
        data = {"username": usr_name,
                "password": pswrd}

        x = requests.post(url, json = data)
        response = json.loads(x.text)
        _id = ''
        if response["message"] == 'Login successfully.':
            if response['data']['role'] == 'STUDENT':
                clear_screen()
                student_loop(usr_name)
            elif response['data']['role'] == 'TUTOR':
               clear_screen()
               tutor_loop(usr_name)
            elif response['data']['role'] == 'FACULTY':
               clear_screen()
               fac_loop(usr_name)
            elif response['data']['role'] == 'ADMIN':
               clear_screen()
               admin_loop(usr_name)
        else:
            print(response['message'], "\n")
            
               

    except HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')
      


def reg(cmd, cmd_list):
   email = ''
   usr = ''
   ext = ''
   
   try:
      if len(cmd_list) == 3 and cmd_list[1] == '-e':
         email = cmd_list[2]
         usr = email.split('@')[0]
         ext = email.split('@')[1]
         ext = ext.lower()
         
         if ext != 'una.edu':
            print('please enter a valid UNA email address')
            return

         else:
            pswrd = getpass.getpass(prompt = 'Password> ')
            valid = verifyPswrd(pswrd)
            while valid == -1:
               pswrd = getpass.getpass(prompt = 'Password> ')
               valid = verifyPswrd(pswrd)

            try:
               url = 'https://quanthu.life/tutorapp/users'
               data = {'username': usr, 'email': email,
                       'password': pswrd, 'role': 'STUDENT',
                       'isActive': True}
               x = requests.post(url, json = data)
      
            except HTTPError as http_err:
               print(f'HTTP error occured: {http_err}')
            except Exception as err:
               print(f'Error: {err}')
               
      else:
         print('Error: Invalid arguments\n')
         return
      
   except IndexError as ind:
      print('please enter a valid UNA email address\n')
      return
   except Exception as excep:
      print(f'Error: {excep}\n')
      return



def verifyPswrd(pswrd):
   SpecialSym=['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?'\
                '(', ')', '/', '|', '}', '{', '~', '`', ':']
   return_val = 1
   if len(pswrd) < 8:
      print('the length of password should be at least 8 char long')
      return_val = -1
   if not any(char.isdigit() for char in pswrd):
      if not any(char in SpecialSym for char in pswrd):
         print('the password should have at least one of the symbols $@# or a digit')
         return_val = -1
   if not any(char.isupper() for char in pswrd):
      print('the password should have at least one uppercase letter')
      return_val = -1
   if not any(char.islower() for char in pswrd):
      print('the password should have at least one lowercase letter')
      return_val = -1

   return return_val



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
            print('Error: Invalid command\n')
             
      except KeyboardInterrupt as e:
         cmd = 'exit'
         print()
      except IndexError as ind:
            if cmd == '\r' or '\n': continue
            else:
                print('Error: Wrong number of arguments\n')
                continue
      '''
      except Exception as exc:
         print(f'Error: Internal Error \'{exc}\'\n')
         continue
      '''

