def game():
    return 1008

score=game()
with open("hiscore.txt") as f:
    hiscore=f.read()
if(hiscore!=""):
    hiscore=int(hiscore)
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score)) # write only writes a string not integer
elif(hiscore==''):
    with open("hiscore.txt","w") as f:
        f.write(str(score))