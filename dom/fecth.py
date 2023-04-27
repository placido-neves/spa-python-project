import requests

class Fecth:
    def __init__(self,urlBase):
        self.urlBase =  urlBase
    
    def get(self, path):
        js  = requests.get(self.urlBase+path)
        return js.json() 
    
    def post(self,path,data):
        js = requests.post(self.urlBase+path, data=data)
        return js.json()
        
    def path(self,path,data):
        js = requests.patch(self.urlBase+path,data=data)
        return js.json()
    
    def delete(self,path):
       js = requests.delete(self.urlBase+path)
       return js.json()