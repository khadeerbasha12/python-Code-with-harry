class Employee:
    company="Google"

khadeer =Employee()
naval = Employee()
print(khadeer.company)
print(naval.company)
Employee.company="YouTube"
print(khadeer.company)
print(naval.company)