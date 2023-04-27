from dom.singleton import Singleton

class Render(metaclass = Singleton):
  def __init__(self):
    self._file = None
  
  def getComponets(self):
    return self._file
        
  def setComponents(self, data):
    self._file =  data
  
class JS(metaclass = Singleton):
  def __init__(self):
    self.js = {}
  
  def getComponets(self):
    return self.js    
        
  def setComponents(self, routes,path):
    self.js[routes] = path
  
class Effect(metaclass = Singleton):
  def __init__(self):
    self._file = {}
  
  def getComponets(self):
    return self._file   
        
  def setComponents(self, name, data):
    self._file[name] = data