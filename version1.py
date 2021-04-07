import os
import getpass
import student

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')


def getHelp():
   print("\nTo login, simply type 'login' ")
   print("If you do not have an account, type 'regact "
         "-yourUsername -yourPassword' ")
   print("Otherwise, type 'exit' to close the program\n")


def login():
   while True:
      usr = input('\nUsername> ')
      if not len(usr) > 0:
         print("Username cannot be blank")
      else:
         break
      
   while True:
      pswrd = getpass.getpass(prompt = 'Password> ')
      if not len(pswrd) > 0:
         print("Password cannot be blank")
      else:
         break
   

if __name__ == "__main__":
   clear_screen()
   print('********************************************************************************')
   print('*                        University of North Alabama                           *')
   print('*                    Tutor Appointment Management System                       *')
   print('*                                                                              *')
   print('*  For help type --help                                                        *')
   print('********************************************************************************')

   try:
      cmd = (input('> '))
      while cmd != "exit":
         if cmd == "--help":
            getHelp()

         elif cmd == "login":
            login()

         elif cmd == "exit":
            clear_screen()
            exit
       
         elif cmd == "mkapt":
            student.mkapt()
         cmd = (input('> '))
          
   except KeyboardInterrupt as e:
      print(e)
   except Exception as e:
      print(e)
   finally:
      exit
