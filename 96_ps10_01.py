class Programmer:
    company="Microsoft"
    def __init__(self,name,id,mob):
        self.name=name
        self.id=id
        self.mob=mob

    def printer(self):
        print(f"company={self.company}\nname={self.name}\nid={self.id}\nmobile number={self.mob}\n")

obj=Programmer("khadeer",12345,9652766974)
obj1=Programmer("naval",12345,965276974)
obj.printer()
obj1.printer()
