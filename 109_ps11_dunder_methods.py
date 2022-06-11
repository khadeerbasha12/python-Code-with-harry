class Number:
    def __init__(self,num) -> None:
        self.num=num
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num

    def __mul__(self,num2):
        print("Lets multiply")
        return self.num*num2.num
    # it returns a string 
    def __str__(self):
        return f"Decimal Number:{self.num}"
    # it returns the length of the numbe which is 1
    def __len__(self):
        return 1


n1=Number(10)
print(n1)
print(len(n1))