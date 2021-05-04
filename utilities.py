import os
import requests
import json
import getpass

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')

def psr(usr):
   url = 'https://quanthu.life/tutorapp/users'
   usr_id = ''
   req = requests.get(url)
   resp = json.loads(req.text)
   
   if resp['errorCode'] == 200:
      for item in resp['data']:
         if usr == item['username']:
            usr_id = item['_id']
            new_pswrd = getpass.getpass(prompt = 'New Password>')
            ver_pswrd = getpass.getpass(prompt = 'Confirm Password')

            while new_pswrd.strip() != ver_pswrd.strip():
               print('Your passwords did not match, please try again')
               new_pswrd = getpass.getpass(prompt = 'New Password> ')
               ver_pswrd = getpass.getpass(prompt = 'Confirm Password> ')
      
            update_url = 'https://quanthu.life/tutorapp/users/' + usr_id
            data = {'_id': item['_id'],
                    'username': item['username'],
                    'email': item['email'],
                    'password': new_pswrd,
                    'phone': item['phone'],
                    'role': item['role'],
                    'lastActivityDateTime': item['lastActivityDateTime'],
                    'isActive': item['isActive']}
      
            update = requests.put(update_url, json = data)
            update_resp = json.loads(update.text)
            if update_resp['errorCode'] == 200:
               print('Your password has been reset')

            else:
               print (update_resp['message'])

if __name__ == '__main__':
   psr('hbrown3')
