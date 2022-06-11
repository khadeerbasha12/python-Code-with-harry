#SINGLE INHERITANCE

class Employee:
    company = "Google"  # Base class

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"  # Derived class
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)