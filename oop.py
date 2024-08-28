class vvit:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

class cse(vvit):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation_year=year

    def welcome(self):
        print("welcome",self.firstname,self.lastname,"to the class of ",self.graduation_year)
x=cse("salman","faris",2025)
x.welcome()
