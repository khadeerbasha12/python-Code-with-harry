class C2dVec:
    def __init__(self,i,j) -> None:
        self.i=i
        self.j=j
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j" 
        
class C3dVec (C2dVec):
    def __init__(self,i,j,k) -> None:
        super().__init__(i,j)
        self.k=k

        # str is same as toString function in java lang
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k" 

c2d=C2dVec(1,2)
c3d=C3dVec(1,2,3)
print(c2d)
print(c3d)