mydict= {
    "fast": "in a quick manner",  # dictionary is always unordered
    "khadeer": "a fast learner",
    "marks": [1,3,2,4],
    "anotherdict":{          # we can create nested dictionaries like this--->
        "khadeer":"player",
    }
}
mydict["marks"]=[10,23,34]
print(mydict["fast"])
print(mydict["marks"])
print(mydict["anotherdict"]["khadeer"])