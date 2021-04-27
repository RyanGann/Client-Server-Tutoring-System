
import requests
import json

def tutorloop(usr, pswrd):
    #curTutor = Tutor(usr, pswrd)
    #getSched(usr)
    name = usr.split("@")[0]
    
    cmd = ""
    while cmd != "logout":

        try:
            cmd = (input(f'{name}> '))
            cmdList = cmd.split()

            if cmdList[0] == "papt":
                papt(name)
            elif cmdList[0] == "capt":
                capt()
            elif cmdList[0] == "aapt":
                aapt(cmdList[1], cmdList[2], cmdList[3], cmdList[4])
            elif cmdList[0] == "edapt":
                edapt()
            elif cmdList[0] == "dapt":
                dapt()
            elif cmdList[0] == "--help":
                getHelp()
            elif cmdList[0] == "psr":
                curTutor.pswrdReset()
            elif cmdList[0] == 'exit':
                clear_screen()
                return
            elif cmd != "logout":
                print("Error: invalid command")
        except IndexError as ind:
            print("Error: wrong number of arguements")
            continue
        except KeyboardInterrupt as kybrd:
            return

# This function prints all appointments by tutor _id
def papt(usr):
    #print("Get all current appointments from server")
    
    users_url = 'https://quanthu.life/tutorapp/users'
    x = requests.get(users_url)
    users = json.loads(x.text)
    if users['errorCode'] == 200:
      print(users['message'])
    elif users['errorCode'] == 404:
      print(users['message'])

    for item in users['data']:
      if usr == item['username']:
        print("inside if inside for")
        tutor_id = item['_id']
        print(tutor_id)
        break

    
    url = 'http://quanthu.life:8000/schedule/'
    tutor_url = url + tutor_id
    x = requests.get(tutor_url)
    tutor_sched = json.loads(x.text)
    if tutor_sched['errorCode'] == 200:
      print(tutor_sched['message'])
      print(tutor_sched)
    elif tutor_sched['errorCode'] == 404:
      print(tutor_sched['message'])

    

def capt():
    print("hey")
    
def aapt(id, date, from_time, end_time):
    url = 'http://quanthu.life:8000/schedule'
    data = {'tutor_id': id,
            'date': date,
            'from time': from_time,
            'end_time': end_time}

    x = requests.post(url, json = data)

def edapt():
    print("Edit appointment with new date, student, or course number")

def dapt():
    print("Delete an appointment by given date, student, and course number")

def getHelp():
    print("papt\tPrint all appointments\n")
    print("capt\tComplete and appointment by using the key to lookup\n")
    print("aapt\tCreate a new appointment\n")
    print("edapt\tEdit specific appointment date, student, and course number\n")
    print("dapt\tEdit current appointment with new date, tutor, or course number\n")
    print("dapt\tDelete appointment by a given date, tutor, and course number\n")
    print("psr\tPassword reset that takes old and then new password\n")
