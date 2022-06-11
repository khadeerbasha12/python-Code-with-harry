n=3
for i in range (3): # end=" " --> does not allllow to go to next line
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
  