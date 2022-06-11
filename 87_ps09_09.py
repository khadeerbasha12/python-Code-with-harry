with open("sample.txt","r") as f:
    d=f.read()
with open("copy.txt","r") as f:
    d1=f.read()
if(d==d1):
    print("same")
else:
    print("not same")