from Factory import Factory

class Chassis(Factory):
    def __str__(self):
        return type(self).__name__.ljust(21) 

class MercedesChassis(Chassis):
    downforceMult = 1.021

class FerrariChassis(Chassis):
    downforceMult = 1.015  

class RedBullChassis(Chassis):
    downforceMult = 1.018 

class RenaultChassis(Chassis):
    downforceMult = 1.007

class AlfaRomeoChassis(Chassis):
    downforceMult = 1.002

class MclarenChassis(Chassis):
    downforceMult = 1.009

class RacingPointChassis(Chassis):
    downforceMult = 1.001

class ToroRossoChassis(Chassis):
    downforceMult = 1.005

class HaasChassis(Chassis):
    downforceMult = 1.002

class WilliamsChassis(Chassis):
    downforceMult = 0.981
