class Employee:
    company="Google"
    ecode=120

class FreeLancerr:
    company="YouTube"
    level=0
    def upgradeLevel(self):
        self.level+=1

    #-->multiple inheritance
class Programmer(Employee,FreeLancerr):
    name="Khadeer"

obj = Programmer()
print(obj.level)
obj.upgradeLevel()
print(obj.level)