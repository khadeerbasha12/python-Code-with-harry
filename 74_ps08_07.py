def remove(s,w):
    s=s.replace(w,"")
    return s.strip()
s=input("enter the string")
w=input("enter the word")
str=remove(s,w)
print(str)