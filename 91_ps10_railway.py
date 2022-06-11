class RailwayForm:
    formType = "RAILWAT FORM"
    def printData(self):
        print("the name is=",self.name)
        print("the train is=",self.train)

khadeer =RailwayForm()  #object instantiation
khadeer.name="khadeer"   #initialising name
khadeer.train="Rajdhani Express"
khadeer.printData()