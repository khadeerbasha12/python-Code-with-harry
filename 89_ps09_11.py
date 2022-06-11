import os
with open("copy.txt","r") as f:
    d=f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(d)
os.remove("copy.txt")