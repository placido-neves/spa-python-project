from bs4 import BeautifulSoup


class Component():
    def compy(self,css):
        def decorator(function):
            def wrapper():
                content =  BeautifulSoup(function(),  features='html.parser')
                return{'html':content, "css":css}      
            return wrapper
        return decorator
    
    def main(self,css):
        def decorator(function):
            def wrapper():
                html = ""
                tema = css
                for route in list(function()['routes'].keys()):                   
                    if route != "title":
                        for content in function()['routes'][route]:
                            html += str(content["html"])
                            if css in content :
                                tema += '\n' + content['css']
                copied = function().copy()
                for route in list(function()['routes'].keys()):
                    if route != 'title':
                        copied['routes'][route] = {'html':html, "css":tema}
                return copied
                    
            return wrapper
        return decorator
    
    def effect(self,name):
        content = BeautifulSoup(f"<span id = {name}</span>", features="html.parser")
        return {"html":content}
    
    def staticFile(self,source):
        f = open(source)
        return f.read()
    
    def map(self, function, arr):
        save = list(map(lambda a: function(a), arr))
        arrString = ' '.join(s for s in save)
        return arrString

    def filter(self,condition ,function, arr):
        filtered = list(filter(lambda a: condition(a), arr))
        save = list(map(lambda f: function(f),filtered))
        arrString = ' '.join(s for s in save)
        return arrString
    

    """ 
        
                for content in function()['routes'][route]:
                            html += content[html]
                            if css in content :
                                tema += '\n' + content['css']
                copied = function().copy()
                for route in list(function()['routes'].keys()):
                    if route != 'title':
                        copied['routes'][route] = {'html':html, "css":tema}
                return copied"""