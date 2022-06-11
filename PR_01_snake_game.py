import random
# snake water gun /// rock paper scissor
def game(comp,b):
    if comp==b:
        return None
    elif(comp=='s'):
        if(b=='w'):
            return False
        elif b=='g':
            return True
    elif(comp=='w'):
        if(b=='g'):
            return False
        elif b=='s':
            return True
    elif(comp=='g'):
        if(b=='s'):
            return False
        elif b=='w':
            return True

print("computer Turn: Snake (1) or Water (2) or Gun(3)?")
ran_num =random.randint(1,3) #selects a random num among 1,2,3
if(ran_num==1):
    comp='s'
elif(ran_num==2):
    comp='w'
else:
    comp='g'
b=input("palyer's Turn: Snake (s) or Water (w) or Gun(g)?")
print("you chose=",b)
print("computer chose=",comp)
game1=game(comp,b)
if(game1==None):
    print("TIE")
elif(game1==True):
    print("you win")
else:
    print("you lose")