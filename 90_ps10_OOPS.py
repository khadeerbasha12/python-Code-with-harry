# a=14
# b=34
# print("the sum is=",a+b)

class Number:
    def sum(self):
        return self.a+self.b

num=Number()
num.a=12
num.b=34
s=num.sum()
print("the sum is=",s)