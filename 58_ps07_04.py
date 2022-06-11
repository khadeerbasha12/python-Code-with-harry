n=int(input("enter the number=\n"))
a=True
for i in range (2,n): # to see b/w including 2 and excluding n
    if n%i==0:
        a=False
        break
if a==True:
    print("it is a prime number")
else:
    print("not a prime number")
