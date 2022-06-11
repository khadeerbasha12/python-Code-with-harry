def percent(marks):
    s=0
    a=len(marks)*100
    for(i) in range (len(marks)):
        s=s+marks[i]
    return (s/a)*100

 # a function can be defined by def keyword

marks=[45,78,86,77]
p=percent(marks)
print(p)
