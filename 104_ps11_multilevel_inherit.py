class Person:
    country="India"
    def takeBreath(self):
        print("iam a person taking breath")
class Employee(Person):
    company="honda"
    def getSalary(self):
        print("salary=",self.salary)
    def takeBreath(self):
        print("iam an emplyee who is taking breath")


class Programmer(Employee):
    company="Google"
    def takeBreath(self):
        print("im an programmer who is taking breath")
    
    def getSalary(self):
        print("there is no salary to programmer")

p=Person()
p.takeBreath()
e=Employee()
e.takeBreath()
print(e.company)
pr=Programmer()
print(pr.company)
pr.takeBreath()
print(pr.country)