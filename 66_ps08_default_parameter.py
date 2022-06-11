def greet(n="Stranger"):    #  if no value is passed the default value will become stranger
     return "good day, "+n
a=input("enter the name")
# s=greet(a)
s=greet() # no value is passed then "stranger" will come
print(s)