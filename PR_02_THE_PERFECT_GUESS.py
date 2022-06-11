import random

rand_num=random.randint(1,100)
user=None
guesses=5
print("you have 5 guesses")
while(guesses>0):
    user=int(input("enter your guess "))
    if(user==rand_num):
        print(f"Congratulations\n  you Guessed it right! the correct number is = {rand_num}")
        break
    elif(user>rand_num):
        print("you guessed the larger number! enter a lower number")
    elif(user<rand_num):
        print("you guessed the lower number! enter a larger number")
    guesses-=1
    print(f"you are left with {guesses} chances to guesss the correct number")
    print("\n")
if(guesses==0):
    print(f"\nyou are out of your chances\n  The correct answer is {rand_num}\n")