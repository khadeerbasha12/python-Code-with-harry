class Train:
    def __init__(self,name,fare,seats) -> None:
        self.name=name
        self.fare=fare
        self.seats=seats
    def getInfo(self):
        print(f"************\nthe name of the train={self.name}\n the seats available are={self.seats}")
    def fareInfo(self):
        print(f"the fare is= Rs.{self.fare}\n")
    def bookTicket(self):
        if(self.seats>0):
            print(f"your tickrt has been booked! your seat number is={self.seats}")
            self.seats-=1
        else:
            print("sorry this is full! kindly try in tatkal")
    def cancelTicket(self):
        pass
intercity =Train("Intercity Express= 14041",12345,2)
intercity.getInfo()
intercity.fareInfo()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()