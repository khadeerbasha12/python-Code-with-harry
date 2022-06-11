f=open("poems.txt","r")
d=f.read()
if(d.find("twinkle")==-1):
    print("not found")
else:
    print("found")