from dom.singleton import Singleton

class AddCDN(metaclass = Singleton):
  def __init__(self):
    self.link = []
    self.script = []
    
  def addLink(self,*args):
    self.link = args
  
  def get_link(self):
    return self.link
    
  def addScript(self,*args):
    self.script = args
    
  def get_script(self):
    return self.script