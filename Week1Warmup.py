Name = "Ben"
FavNumber = 11
sqrd = FavNumber * FavNumber

for i in range(0,sqrd+1):
    if i == 0:
        print(Name)
    else:
        print (i)

class Engineer:
    def __init__(self,name,type,years):
        self.name = name
        self.type = type
        self.years = years
    def getname(self):
        print("Enginers Name: " + self.name)
    def gettype(self):
        print("Engineering Field: " + self.type)
    def getexperience(self):
        print("Years of Experience: " + self.years)

Eng1 = Engineer("Bob","Civil","11")
Eng2 = Engineer("Kev","Elec","12")

Eng1.getname()
Eng1.gettype()
Eng1.getexperience()
Eng2.getname()
Eng2.gettype()
Eng2.getexperience()