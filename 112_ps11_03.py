class Employee:
    sal=1000
    increment=2

    @property
    def salaryAfterIncrement(self):
        return self.sal*self.increment
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment=sai/self.sal
e=Employee()
print(e.salaryAfterIncrement)

print(e.increment)
e.salaryAfterIncrement=3000
print(e.increment)
