print("enter 4 numbers")
s=0
for i in range (4):
    a=int(input())
    if(a>s):
        s=a
print("the maximum number entered is=", s)