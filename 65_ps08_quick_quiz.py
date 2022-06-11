def greet(n):
    if(n == ""):
        return "good day, Stranger"
    else:
        return "good day, "+n
a=input("enter the name")
s=greet(a)
print(s)