with open("sample.txt","r") as f:
    con= f.read()

con=con.replace("donkey","#$^&%#$")
with open("sample.txt","w") as f:
    f.write(con)