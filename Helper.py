from Session import *
from Track import *
from Turn import *
from Tyre import *
from Car import *
from Engine import *
from Chassis import *

def tyreConstructor(arg):
    constructorDict={
        "SoftTyre": SoftTyre(),
        "MediumTyre": MediumTyre(),
        "HardTyre": HardTyre()}
    return constructorDict.get(arg,random.choice([SoftTyre(),MediumTyre(),HardTyre()]))

def turnConstructor(arg):
    constructorDict={
        "Straight": Straight(*arg),
        "LowSpeedTurn": LowSpeedTurn(*arg),
        "MediumSpeedTurn": MediumSpeedTurn(*arg),
        "HighSpeedTurn": HighSpeedTurn(*arg)}
    return constructorDict.get(arg[1])

def engineConstructor(arg):
    constructorDict={
        "FerrariEngine": FerrariEngine(),
        "MercedesEngine": MercedesEngine(),
        "HondaEngine": HondaEngine(),
        "RenaultEngine": RenaultEngine()}
    return constructorDict.get(arg)

def chassisConstructor(arg):
    constructorDict={
        "Ferrari": FerrariChassis(),
        "Mercedes": MercedesChassis(),
        "RedBull": RedBullChassis(),
        "Renault": RenaultChassis(),
        "Mclaren": MclarenChassis(),
        "Haas": HaasChassis(),
        "AlfaRomeo": AlfaRomeoChassis(),
        "ToroRosso": ToroRossoChassis(),
        "RacingPoint": RacingPointChassis(),
        "Williams": WilliamsChassis()}
    return constructorDict.get(arg)

def pitStopConstructor(arg):
    constructorDict={
        "S": random.choice([MediumTyre(),HardTyre()]),
        "M": random.choice([SoftTyre(),HardTyre()]),
        "H": random.choice([MediumTyre(),SoftTyre()])}
    return constructorDict.get(arg)