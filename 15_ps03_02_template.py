a="Dear <|NAME|>,\n\tYou Are Selected!\n\nDate: <|DATE|>"
name=input("enter the name\n")
date=input("enter the date\n")
a=a.replace("<|NAME|>",name)
a=a.replace("<|DATE|>",date)
print(a)