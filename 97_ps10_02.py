from math import sqrt


class Calculator:
    def __init__(self,n) -> None:
        self.n=n

    def square(self):
        print(f"the square is={self.n*self.n}")
    def cube(self):
        print(f"the cube is={self.n*self.n*self.n}")
    def sqroot(self):
        print(f"the square root is={sqrt(self.n)}")

a=int(input("enter the number\n"))
obj=Calculator(a)
obj.square()
obj.cube()
obj.sqroot()