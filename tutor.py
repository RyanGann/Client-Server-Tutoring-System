
import requests
import json
from utilities import clear_screen

def tutor_loop(usr, pswrd):
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
                aapt()
            elif cmdList[0] == "edapt":
                edapt()
            elif cmdList[0] == "dapt":
                dapt()
            elif cmdList[0] == "--help":
                getHelp()
            elif cmdList[0] == "psr":
                pswrdReset()
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
    tutor_id = input("Enter tutor id")
    
    url = 'http://quanthu.life:8000/appointment/'
    tutor_url = url + tutor_id
    x = requests.get(tutor_url)
    tutor_sched = json.loads(x.text)
    if tutor_sched['errorCode'] == 200:
      print(tutor_sched['message'])
      print(tutor_sched)
    elif tutor_sched['errorCode'] == 404:
      print(tutor_sched['message'])

    

def capt():
    id = input("Enter the appointment id that you would like to complete: ")
    
def aapt(id, date, from_time, end_time):

    id = input("Enter tutor_id: ")
    date = input("Enter date of appointment: ")
    from_time = input("Enter start time of appointment: ")
    end_time = input("Enter end time of appointment: ")


    url = 'http://quanthu.life:8000/appointment/'
    data = {'tutor_id': id,
            'date': date,
            'from time': from_time,
            'end_time': end_time}

    x = requests.post(url, json = data)

def edapt():
    id = input("Enter the id of the appointment you would like to edit: ")

    tutor_id = input("Enter the id of the tutor: ")
    student_id = input("Enter the id of the student: ")
    date = input("Enter the date of the appointment: ")
    from_time = input("Enter the start time of the appointment: ")
    end_time = input("Enter the end time of the appointment: ")

    data = {
        "_id": id,
        "tutor_id": tutor_id,
        "student_id": student_id,
        "date": date,
        "from_time": from_time,
        "end_time": end_time
    }

    url = 'http://quanthu.life:8000/appointment/' + id
    response = requests.put(url, json = data)

    if response.status_code == 200:
        print("Successfully edited selected admin")
    elif response.status_code == 404:
        print("Unsuccessful request")

def dapt():
    id = input("Enter the id of the appointment you'd like to delete: ")

    url = 'http://quanthu.life:8000/appointment/' + id
    response = requests.delete(url, data = "deleting appointment")
    if response.status_code == 200:
        print("Successfully edited selected admin")
    elif response.status_code == 404:
        print("Unsuccessful request")

def getHelp():
	infile = open("help_tutor.txt", "r")

	lines = infile.readlines()

	for line in lines:
		print(line, end = "")

	print()
	    
	infile.close()
