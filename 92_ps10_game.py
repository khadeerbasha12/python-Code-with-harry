class Remote:
    #methods can be defined
    pass


class Player:
    def moveRight(self):
        pass
    def moveLeft(self):
        pass
    def mmoveTop(self):
        pass

player1 =Player()
r1=Remote()
if(r1.isLeftPressed()):
    player1.moveLeft()