import os

class User():
    email = ""
    name = ""
    password = ""


    def pswrdReset(self):
        newPswrd, check = "", "."
        while newPswrd != check:
            while True:
                newPswrd = input('Please enter your new password: ')
                if not len(newPswrd) > 0:
                    print('Password can not be blank')
                else:
                    break

            while True:
                check = input('Please re-enter your new password: ')
                if not len(check) > 0:
                    print('Password can not be blank')
                else:
                    break
 
            
            if newPswrd != check:
                print('\nYour passwords did not match, please try again')
            else:
                password = newPswrd
        
