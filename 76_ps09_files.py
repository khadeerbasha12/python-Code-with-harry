# use open to oepn the file
f=open("py.txt","w")
f.write("hi good morning")
f.close()
f=open("py.txt","r") #  by default there read mode
data=f.read() # read(5) --> read upto 5 char
print(data)
f.close()