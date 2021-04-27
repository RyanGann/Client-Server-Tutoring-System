import os

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')
