class Vector:
    def __init__(self,list) -> None:
        self.list=list
        
    def __str__(self) -> str:
        return f"{self.list[0]}i + {self.list[1]}j + {self.list[2]}k"

v1=Vector([1,4,6])  # giving a list as input
v2 = Vector([1,6,9])
print(v1)
print(v2)