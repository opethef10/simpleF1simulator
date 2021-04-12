class Turn:
    # def __new__(cls, subclassName, *args, **kwargs):
        # subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        # subclass = subclassDict[subclassName]
        # return super().__new__(subclass)
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        subclass = subclassDict[subclassName]
        return subclass(*args, **kwargs)
    
    def __init__(self,turnNo,turnType,length,avgSpeed):
        self.turnNo=turnNo
        self.turnType=turnType
        self.length=length
        self.avgSpeed=avgSpeed
    
    def __repr__(self):
        return "\n\t\tturnNo: {:<3} turnType: {:<16} length: {:<7} avgSpeed: {:<6}".format(self.turnNo,self.turnType,self.length,self.avgSpeed)    


class HighSpeedTurn(Turn):
    def __init__(self,turnNo,turnType,length,avgSpeed):
        super().__init__(turnNo,turnType,length,avgSpeed)
        self.wearMult=3.0

class MediumSpeedTurn(Turn):
    def __init__(self,turnNo,turnType,length,avgSpeed):
        super().__init__(turnNo,turnType,length,avgSpeed)
        self.wearMult=2.0

class LowSpeedTurn(Turn):
    def __init__(self,turnNo,turnType,length,avgSpeed):
        super().__init__(turnNo,turnType,length,avgSpeed)
        self.wearMult=1.0

class Straight(Turn):
    def __init__(self,turnNo,turnType,length,avgSpeed):
        super().__init__(turnNo,turnType,length,avgSpeed)
        self.wearMult=0.1    