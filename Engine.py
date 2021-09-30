from Factory import Factory

class Engine(Factory):    
    def __str__(self):
        return type(self).__name__.ljust(16) 

class MercedesEngine(Engine):
    multiplier = 1.003   

class FerrariEngine(Engine):
    multiplier = 1.019 

class HondaEngine(Engine):
    multiplier = 0.998

class RenaultEngine(Engine):
    multiplier = 0.996