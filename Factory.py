class Factory:
    @classmethod
    def create(cls, subclassName, *args, **kwargs):
        for subclass in cls.__subclasses__():
            if subclass.__name__ == subclassName:
                return subclass(*args, **kwargs)