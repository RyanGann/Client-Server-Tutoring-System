from user import User

class Admin(User):

    def adad():
        print("Add a new admin account")

    def edad():
        print("Edit an admin's email, name, or password")

    def delad():
        print("Delete an admin's account by email")

    def adfac():
        print("Add a new faculty account")

    def edfac():
        print("Edit a faculty's email, name, or password")

    def delfac():
        print("Delete a faculty's account by email")

    def adtut():
        print("Add a new Tutor account")

    def edtut():
        print("Edit a tutor's email, name, or password")

    def deltut():
        print("Delete a tutor's account by email")

    def adts():
        print("Add a new schedule object to a given tutor")

    def edts():
        print("Change a given tutor's availability schedule")

    def delts():
        print("Delete a given tutor's availability schedule")

    def psa():
        print("Purge a student account by email")

    def papt():
        print("Purge an appointment by given date")

    def rnrpt():
        print("Run a given report")

    def srpt():
        print("Schedule a report to be emailed periodically")
        
    def gethelp():
        print("adad\tAdd a new admin with an email, name, and password\n")
        print("edad\tEdit an admin's email, name, or password\n")
        print("delad\tDelete an admin's account\n")
        print("adfac\tAdd a new faculty with an email, name, and password\n")
        print("edfac\tEdit a faculty's email, name, or password\n")
        print("delfac\tDelete a faculty's account\n")
        print("adtut\tAdd a new tutor with an email, name, and password\n")
        print("edtut\tEdit a tutor's email, name, or password\n")
        print("deltut\tDelete a tutor's accountd\n")
        print("adts\tAdd a new availability schedule for a given tutor\n")
        print("edts\tEdit a given tutor's availability schedule\n")
        print("delts\tDelete a given tutor's availability schedule\n")
        print("psa\tPurge a given student's account\n")
        print("papt\tPurge appointment data by given date\n")
        print("rnrpt\tRun given report\n")
        print("srpt\tSchedule a report to be emailed periodically\n")
        print("psr\tPassword reset that takes old and then new password\n")

