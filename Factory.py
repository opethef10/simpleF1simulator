class Factory:
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        subclassDict = {subcls.__name__: subcls for subcls in cls.__subclasses__()}
        subclass = subclassDict[subclassName]
        return subclass(*args, **kwargs)