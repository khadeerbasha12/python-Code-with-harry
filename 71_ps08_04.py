def sum_rec(n):
    if(n==0):
        return 0
    return n+sum_rec(n-1)

a=int(input("enter the number"))
s=sum_rec(a)
print(s)
