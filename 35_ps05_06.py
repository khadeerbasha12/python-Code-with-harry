dict={}
a=input("enter your 1st favourite language\n")
b=input("enter your 2nd fav language\n")
c=input(("enter your 3rd fav language\n"))
dict['1st']=a #  key   :   value
# dict['1st']=b  it does not stores the similar keys evenm if the values are different
dict['2nd']=b # values cannot be unique
dict['3rd']=c
print(dict)