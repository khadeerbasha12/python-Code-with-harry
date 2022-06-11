# operator overloading
class Number:
    def __init__(self,num) -> None:
        self.num=num
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num*num2.num

n1=Number(10)
n2=Number(10)
# Operator can be use to class 
# # there are several pre defind methods like
# addition-->__add__
# subtractioon-->__sub__
# multiply-->__mul__
# division-->__truediv__
print(n1+n2)
print(n1*n2)