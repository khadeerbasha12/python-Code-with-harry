from hashlib import new


class Vector:
    def __init__(self,list) -> None:
        self.list=list
        
    def __str__(self) -> str:
        str1=''
        index=0
        for i in self.list:
            str1+=f" {i}a{index} +"
            index+=1
        return str1[:-1]

    def __add__(self,list2):
        if (len(self.list)==len(list2.list)):
            newList=[]
            for i in range(len(self.list)):
                newList.append(self.list[i]+list2.list[i])
            return Vector(newList)
        else:
            print("the length is not same due to which the addition is failed")
            pass
            
    def __mul__(self,list2):
        if(len(self.list)==len(list2.list)):
            sum=0
            for i in range(len(self.list)):
                sum+=self.list[i]*list2.list[i]
            return sum
        else:
            print("unable to perform multiplication due to unequal legth of list given")
            pass


    def __len__(self):
        return len(self.list)


v1=Vector([1,4,6,4])  # giving a list as input
v2 = Vector([1,6,9,7])
print(v1+v2)
print(v1*v2)
# print(len(v1))
# print(len(v2))