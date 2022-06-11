# BY USING FOR LOOP
def fact_iter(n):
    p=1
    for i in range(n):
        p=p*(i+1)
    print(p)

  #   RECCURSION
def fact_rec(n):
    if(n==0 or n==1):
        return 1
    return n*fact_rec(n-1)

n=int(input("enter the number"))
fact_iter(n)
s=fact_rec(n)
print(s)
