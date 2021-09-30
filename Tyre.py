from Factory import Factory

class Tyre(Factory):
    def __init__(self):
        self.degradation = 0.0
    
    def __str__(self):
        return "{}, degradation:{:.1f}".format(self.compound,self.degradation)
    
    def tick(self,viraj):
        self.degradation += (viraj.length * viraj.wearMult * self.compoundDegrMult) / 1000

class SoftTyre(Tyre):
    speedMult = 1.0
    compoundDegrMult = 1.2
    compound = "S"

class MediumTyre(Tyre):
    speedMult = 0.991
    compoundDegrMult = 0.7
    compound = "M"

class HardTyre(Tyre):
    speedMult = 0.984
    compoundDegrMult = 0.38
    compound = "H"
