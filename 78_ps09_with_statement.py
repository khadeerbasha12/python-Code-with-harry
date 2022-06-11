with open("py.txt","r") as f:
    data=f.readline() # readline()--> used to read a single line
    print(data)
# write with --> with statement
with open("py.txt","w") as f:
   f.write("this is in write mode") # readline()--> used to read a single line
 
