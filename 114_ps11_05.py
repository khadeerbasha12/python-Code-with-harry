from hashlib import new


class Vector:
    def __init__(self,list) -> None:
        self.list=list
        
    def __str__(self) -> str:
        str1=''
        index=0
        for i in self.list:
            str1+=f" {i} a{index}+"
            index+=1
        return str1[:-1]

    def __add__(self,list2):
        newList=[]
        for i in range(len(self.list)):
            newList.append(self.list[i]+list2.list[i])
        return Vector(newList)

    def __mul__(self,list2):
        sum=0
        for i in range(len(self.list)):
            sum+=self.list[i]*list2.list[i]
        return sum

v1=Vector([1,4,6])  # giving a list as input
v2 = Vector([1,6,9])
print(v1+v2)
print(v1*v2)