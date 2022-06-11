c=set()  # this creates an empty set 
print(type(c))
c.add(4)
# we can add values by add methods
c.add(4)  # the set doen't contain repetitive data items
c.add(5)
c.add(5)
c.add(6)
# we cant add list in set/ because it is mutable
# c.add([1,2,3,4])     it throws an error / in the same manner we cant add dict also
c.add((1,2,3,4))  # we can add tupple like this
print(c)
print(len(c))
c.remove(6)
print(c)
s=c.pop()  # it returns the value from set
print(s)  # it pops first element 
print(c)
c.clear() # it removes all values in set
print(c)