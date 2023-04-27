class Observable:
    def __init__(self):
        self._observers = []
        self._state = None
        self._function = []
        self._dicts = []
        
    def subscribe(self, observer):
        self._observers.append(observer)
        
    def notify(self):
        for obs in self._observers:
            obs.update(self)
            
    def set_function(self,value,dict):
        self._function.append(value)
        self._dicts.append(dict)
    
    @property
    def change(self):
        return self._state
    
    @change.setter
    def change(self, value):
        self._state = value
        self.notify()
        
class Observer:
    def __init__(self, observable):
        observable.subscribe(self)
        
    def update(self, observable):
        for func in observable._function:
            for d_list in observable._dicts:
                for d in list(d_list.keys()):
                    if d != "set":
                        func(d,d_list[d]())


subject = Observable()