class Employee:
    company="camel"
    salary=1000
    location="delhi"
    # we can directly change the class attribute but not the instance attribute by tinder method--> __class__
    # def changeSal(self,sal):
    #     self.__class__.salary=sal

    #we can change class attribute by--> @classmethod decorator
    @classmethod
    def changeSal(self,sal):
        self.salary=sal

e=Employee()
print(e.salary)
e.changeSal(1)
print(e.salary)
# by running a --> @classmethod decorator i have changed the value of class attribute
print(Employee.salary)