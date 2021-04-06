import os
import student
import getpass

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')

def login():
   #usr = (input('username> '))
   #pswrd = (input('password> '))

   while True:
        usr = input('Username> ')
        if not len(usr) > 0:
            print("Username can't be blank")
        else:
            break
   while True:
        # This line hides the password that the user is typing 
        pswrd = getpass.getpass(prompt = 'Password> ')
        if not len(pswrd) > 0:
            print("Password can't be blank")
        else:
            break

   # Authenticate username and password



if __name__ == "__main__":
    print('********************************************************************************')
    print('*                        University of North Alabama                           *')
    print('*          Department of Computer Science and Information Systems              *')
    print('********************************************************************************')

    try:
        #cmd = (input('> '))
        #clear_screen()
        #if cmd == "mkapt":
        #    student.mkapt()
        login()
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        exit
