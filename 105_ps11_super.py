class Person:
    def __init__(self) -> None:
        print("initialising person\n")
    country="India"
    def takeBreath(self):
        print("iam a person taking breath")
class Employee(Person):
    def __init__(self) -> None:
        super().__init__()
        print("initialising Employee\n")
    company="honda"
    def getSalary(self):
        print("salary=",self.salary)
    def takeBreath(self):
        super().takeBreath()
        print("iam an employee who is taking breath")


class Programmer(Employee):
    def __init__(self) -> None:
        # calling super class constructor
        super().__init__()
        print("initialising programmer\n")
    company="Google"
    def takeBreath(self):
        # calling base class methods
        super().takeBreath()
        print("im an programmer who is taking breath")
    
    def getSalary(self):
        print("there is no salary to programmer")

# p=Person()
# p.takeBreath()
# e=Employee()
pr=Programmer()
# pr.takeBreath()