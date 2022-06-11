mydict= {
    "fast": "in a quick manner",  # dictionary is always unordered
    "khadeer": "a fast learner",
    "marks": [1,3,2,4],
    "anotherdict":{          # we can create nested dictionaries like this--->
        "khadeer":"player"
    }
}
# print(mydict.keys())
# print(mydict.values())
# print(mydict.items())
print(mydict)
newdict= {
    "hardwork" : "hardwork",
    "fast": "in a slow manner",  # it updates the already existing valu =e with same name into the new one
}
mydict.update(newdict)  #we can update the dictionary like this / we can add new things to dictionary like this-->
print(mydict.get("khadeer"))  #if erroor comes it return none
print(mydict["khadeer"]) #  if error comes it returns erroe

#the difference between get and direct access

print(mydict.get("khadeer2"))  
print(mydict["khadeer2"]) 