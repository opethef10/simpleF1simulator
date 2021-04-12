class Tyre:
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        subclass = subclassDict[subclassName]
        return subclass()
        
    def __init__(self,compound,speedMult,degradation,compoundDegrMult):
        self.speedMult=speedMult
        self.degradation=degradation
        self.compoundDegrMult=compoundDegrMult
        self.compound=compound
    
    def __repr__(self):
        return "{}, degradation:{:.1f}".format(self.compound,self.degradation)
    
    def tick(self,viraj):
        self.degradation+=(viraj.length*viraj.wearMult*self.compoundDegrMult)/1000


class SoftTyre(Tyre):
    def __init__(self,compound="S",speedMult=1.0,degradation=0.0,compoundDegrMult=1.2):
        super().__init__(compound,speedMult,degradation,compoundDegrMult)

class MediumTyre(Tyre):
    def __init__(self,compound="M",speedMult=0.991,degradation=0.0,compoundDegrMult=0.7):
        super().__init__(compound,speedMult,degradation,compoundDegrMult)

class HardTyre(Tyre):
    def __init__(self,compound="H",speedMult=0.984,degradation=0.0,compoundDegrMult=0.38):
        super().__init__(compound,speedMult,degradation,compoundDegrMult)