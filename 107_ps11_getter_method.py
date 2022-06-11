class Employee:
    company="Bharat Gas"
    sal=1234
    sal_bonus=1000
    # tot_sal=sal+sal_bonus

    # same as getter in java
    @property
    def totalSalary(self):
        return self.sal+self.sal_bonus

    # same as setter in java
    @totalSalary.setter
    def totalSalary(self,val):
        self.sal_bonus=val-self.sal

e=Employee()
print(e.sal)
print(e.sal_bonus)
print(e.totalSalary)
e.totalSalary=5800
print(e.sal_bonus)
print(e.totalSalary)
