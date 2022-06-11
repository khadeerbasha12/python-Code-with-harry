with open("sample.txt","r") as f:
    d=f.read()
 # copying a file content to other file
with open("copy.txt","w") as f:
    f.write(d)