class Singleton(type):
    _instaces = {}
    
    def __call__(cls, *args, **kwds) :
        if cls not in cls._instaces:
            instance = super().__call__(*args,**kwds)
            cls._instaces[cls] = instance
        return cls._instaces[cls]