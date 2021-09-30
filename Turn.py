from Factory import Factory

class Turn(Factory):    
    def __init__(self,turnNo,turnType,length,avgSpeed):
        self.turnNo=turnNo
        self.turnType=turnType
        self.length=length
        self.avgSpeed=avgSpeed
    
    def __str__(self):
        return "\n\t\tturnNo: {:<3} turnType: {:<16} length: {:<7} avgSpeed: {:<6}".format(self.turnNo,self.turnType,self.length,self.avgSpeed)    

class HighSpeedTurn(Turn):
    wearMult = 3.0
    downforceCoefficient = 3.0

class MediumSpeedTurn(Turn):
    wearMult = 2.0
    downforceCoefficient = 2.0

class LowSpeedTurn(Turn):
    wearMult = 1.0
    downforceCoefficient = 1.0

class Straight(Turn):
    wearMult = 0.1  
    downforceCoefficient = 0
