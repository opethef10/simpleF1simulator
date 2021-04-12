class Engine:
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        subclass = subclassDict[subclassName]
        return subclass()

class MercedesEngine(Engine):
    def __init__(self):
        self.multiplier=1.003
    def __repr__(self):
        return "<MercedesEngine>".ljust(16)   

class FerrariEngine(Engine):
    def __init__(self):
        self.multiplier=1.019
    def __repr__(self):
        return "<FerrariEngine>".ljust(16)   

class HondaEngine(Engine):
    def __init__(self):
        self.multiplier=0.998
    def __repr__(self):
        return "<HondaEngine>".ljust(16)   

class RenaultEngine(Engine):
    def __init__(self):
        self.multiplier=0.996
    def __repr__(self):
        return "<RenaultEngine>".ljust(16)