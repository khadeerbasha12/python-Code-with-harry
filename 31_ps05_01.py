dict ={
    "tenet" :  "सिद्धांत",
    "digress"  :  "विषय से हटना",
    "fan" : "pankha"
}
print("options are=",dict.keys())
a=input("enter the english word to be translated into english\n")
print("the hindi meaning is=",dict.get(a))