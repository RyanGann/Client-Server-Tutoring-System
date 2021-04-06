import os
import student

def clear_screen():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
       _ = os.system('cls')


if __name__ == "__main__":
    print('********************************************************************************')
    print('*                        University of North Alabama                           *')
    print('*          Department of Computer Science and Information Systems              *')
    print('********************************************************************************')

    try:
        cmd = (input('csis> '))
        clear_screen()
        cmdArray = cmd.split(" ")
        print(cmdArray)
        if cmdArray[0] == "mkapt":
            student.mkapt(cmdArray[1], cmdArray[2], cmdArray[3])
    except KeyboardInterrupt as e:
        print(e)
    except Exception as e:
        print(e)
    finally:
        exit
