print("enter marks of 3 subjects")
s1=int(input("enter first sub marks"))
s2=int(input("enter second sub marks"))
s3=int(input("enter third sub marks"))
if(s1<33 or s2<33 or s3<33):
    print("failed")
elif((s1+s2+s3)/3 <40):
    print("you are failed reason:less toot percent")
else:
    print("passed")