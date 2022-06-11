l1=[1,4,3,6,5,2,8,0,9]
l1.sort()   #there is no need to initialise the sorted list with l1 because it sorts the original list
print(l1)
l1.reverse()
print(l1)
l1.append(10)   # it adds (10) to end of the list
print(l1)
l1.insert(3,100)  #it adds 100 at index 3
print(l1)
l1.pop(3)
print(l1)
l1.remove(3) #it does not serach for index because it searches for the element
print(l1)
print(l1.count(9))