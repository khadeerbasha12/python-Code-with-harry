class Complex:
    def __init__(self,r,i) -> None:
        self.r=r
        self.i=i
    def __add__(self,c):
        return complex(self.r +c.r,self.i+c.i)

    def __mul__(self,c):
        mulReal=self.r*c.r-self.i*c.i
        mulImg=self.r*c.i-self.i*c.r
        return complex(mulReal,mulImg)
    
    def __str__(self) -> str:
        return f"{self.r} +{self.i}i"

c1=complex(1,2)
c2=complex(1,3)
print(c1+c2)
print(c1*c2)