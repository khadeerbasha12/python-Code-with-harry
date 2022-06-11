from random import sample

# we can change self in to any name
class Sample1:
    # def __init__(self,name) -> None:
    #     self.name-name
    def __init__(khadeer,name) -> None:
        khadeer.name=name


obj=Sample1("khadeer")# --> passing the khadder as argument in object instantiation
print(obj.name)
