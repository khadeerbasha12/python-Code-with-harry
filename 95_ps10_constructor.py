class Employee:
    company="Google"
    # name=""
    # sal=0
    # sub=''
#---------------------------------------------------------
    # it is same as constructor in java--> __init__
    # it self as argument as remaining arguments


    def __init__(self,n,s,sub):
        self.name=n
        self.sal=s
        self.sub=sub
        print("employee created")

    @staticmethod   
    def greet():
        print("good morning")
    
    def printer(self):
        print("name=",self.name,"slalary=",self.sal,"subunit=",self.sub)

khadeer=Employee("khadeer",100,"Youtube")
khadeer.greet()
khadeer.printer()