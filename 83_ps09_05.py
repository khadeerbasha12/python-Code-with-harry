words =["naval","pavan","rohanth"]
with open("sample.txt","r") as f:
    con= f.read()
for word in words:
    con=con.replace(word,"#$^&%#$")
with open("sample.txt","w") as f:
    f.write(con)