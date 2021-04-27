from user import User

class Faculty(User):

    def rnrpt():
        print("Run the report of your choosing")

    def srpt():
        print("Schedule a report to be emailed periodically")

    def gethelp():
        print("rnrpt\tRun given report\n")
        print("srpt\tSchedule a report to be emailed periodically\n")
        print("psr\tPassword reset that takes old and then new password\n")