import os
import getpass
from student import studentloop

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')

# Help page pre-login
def getHelp():
   print("\nTo login, simply type 'login' ")
   print("If you do not have an account, type 'regact "
         "-yourUsername -yourPassword' ")
   print("Otherwise, type 'exit' to close the program\n")

'''
   This function recieves the user's input for username and checks that the
   email extensionis '@una.edu'.  If its not, then a proper error is displayed
   and the user is prompted to try again.  Next we take a password that cannot
   be blank from the user.  
'''
def login():
   while True:
      usr = input('\nUsername> ')
      ext = ""
      try:
         ext = usr.split("@")[1]
         ext = ext.lower()
      except IndexError as ind:
         print("please enter a valid UNA email address")
         continue
      if not len(usr) > 0:
         print("Username cannot be blank")
      elif ext != "una.edu":
            print("Username must be official UNA portal email")
      else:
         if checkCred(usr, "password") == 0:
            print("Username does not exists")
            return
         break
      
   while True:
      pswrd = getpass.getpass(prompt = 'Password> ')
      if not len(pswrd) > 0:
         print("Password cannot be blank")
      else:
         break
   authorize(usr, pswrd)


'''
   This function checks the given username and password to determine if the
   loggin in user is a student or a tutor
'''
def checkCred(username, password):
   studFile = open("accounts.txt", "r")
   tutFile = open("tutors.txt", "r")
   students, tutors, studLen, tutLen, ctr, inner, ret = [], [], 0, 0, 0, 1, 0

   for line in studFile:
      students.append(line.split())
      studLen = studLen + 1

   for line in tutFile:
      tutors.append(line.split())
      tutLen = tutLen + 1

   while ctr < studLen:
      if students[ctr][0] == username:
         ret = 1
      while inner < 2:
         if students[ctr][inner] == password:
            ret = ret + 1
         inner = inner + 1
      inner = 1
      ctr = ctr + 1
      
   if ret == 2:
      return 2
   
   ctr = 0
   inner = 1

   while ctr < tutLen:
      if tutors[ctr][0] == username:
         ret = 3
      while inner < 2:
         if tutors[ctr][inner] == password:
            ret = ret + 1
         inner = inner + 1
      inner = 1
      ctr = ctr + 1


   studFile.close()
   tutFile.close()
   return ret
     

'''
   Simple authorization for the moment.  Checks credentials and starts the
   student or tutor loop respectively 
'''
def authorize(usr, pswrd):
   priv = checkCred(usr, pswrd)
   if priv == 2:
      studentloop(usr, pswrd)
   else:
      tutorloop(usr, pswrd)

'''
   Function to validate that a UNA email was given
'''
def verifyEmail(email):
   ext = email.split("@")[1]
   ext = ext.lower()

   if not len(email) > 0:
      print("Username cannot be blank")
      return -1
   elif ext != "una.edu":
      print("Username must be official UNA portal email address")
      return -1
   else:
      return 1


'''
   Function to validate that the password meets the requirements
'''

def verifyPswrd(pswrd):
   SpecialSym=['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?'\
                '(', ')', '/', '|', '}', '{', '~', '`', ':']
   return_val = 1
   if len(pswrd) < 8:
      print('the length of password should be at least 6 char long')
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


'''
   This function takes in the arguements that have been passed to the regact
   command and adds the new account to the accounts file

def reg(cmd, cmdList):

   try:
      if len(cmdList) == 3 and cmdList[1] == "-u":
            
         if verifyEmail(cmdList[2]) == 1:
            if checkCred(cmdList[2], "") == 1:
               print("Error: Username already exists\n")
               return
            print("Error: Username has to be official UNA Portal email address\n")
               
            pswrd = getpass.getpass(prompt = 'Password> ')
            pswrdCheck = verifyPswrd(pswrd)
            
            while pswrdCheck != 1:
               pswrd = getpass.getpass(prompt = 'Password> ')
               pswrdCheck = verifyPswrd(pswrd)
            
            regact(cmdList[2], pswrd)

         # Case for wrong arguement flags
      elif cmdList[1] != "-u":
         print("Error: wrong arguement passed to command")

            
   except IndexError as ind:
      print("Error: wrong number of arguements")

'''

if __name__ == "__main__":
   #clear_screen()
   print('********************************************************************************')
   print('*                        University of North Alabama                           *')
   print('*                    Tutor Appointment Management System                       *')
   print('*                                                                              *')
   print('*  For help type --help                                                        *')
   print('********************************************************************************')

   cmd = ""
   while cmd != "exit":
      try:

         #studentloop()

         cmd = (input('UNA> '))
         cmdList = cmd.split()
      
         if cmdList[0] == "--help":
            getHelp()

         elif cmdList[0] == "login":
            login()

         elif cmdList[0] == "regact":
            reg(cmd, cmdList)
               
         elif cmdList[0] == "exit":
            clear_screen()
            exit

         else:
            print("Error: Invalid command")
             
      except KeyboardInterrupt as e:
         cmd = "exit"
      except IndexError as ind:
         print("Username lookup error\n")
         continue
