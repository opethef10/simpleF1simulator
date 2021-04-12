class Chassis:
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        subclass = subclassDict[subclassName]
        return subclass()

class MercedesChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.021
    def __repr__(self):
        return "<MercedesChassis>".ljust(21)   

class FerrariChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.015
    def __repr__(self):
        return "<FerrariChassis>".ljust(21)   

class RedBullChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.018
    def __repr__(self):
        return "<RedBullChassis>".ljust(21)   

class RenaultChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.007
    def __repr__(self):
        return "<RenaultChassis>".ljust(21) 

class AlfaRomeoChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.002
    def __repr__(self):
        return "<AlfaRomeoChassis>".ljust(21) 

class MclarenChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.009
    def __repr__(self):
        return "<MclarenChassis>".ljust(21) 

class RacingPointChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.001
    def __repr__(self):
        return "<RacingPointChassis>".ljust(21) 

class ToroRossoChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.005
    def __repr__(self):
        return "<ToroRossoChassis>".ljust(21) 

class HaasChassis(Chassis):
    def __init__(self):
        self.downforceMult=1.002
    def __repr__(self):
        return "<HaasChassis>".ljust(21) 

class WilliamsChassis(Chassis):
    def __init__(self):
        self.downforceMult=0.981
    def __repr__(self):
        return "<WilliamsChassis>".ljust(21) 