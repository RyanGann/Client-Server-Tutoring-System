from user import User

class Faculty(User):

    def rnrpt():
        print("Run the report of your choosing")

    def srpt():
        print("Schedule a report to be emailed periodically")

    def gethelp():
        infile = open("help_student.txt", "r")

        lines = infile.readlines()

        for line in lines:
        print(line, end = "")

        print()
	    
        infile.close()
