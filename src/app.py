from dom.compy import Component
from dom.CDN import AddCDN
from src.Components.Nav.index import Nav

com  = Component()
add = AddCDN()

fontAwasome = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css"

add.addLink(fontAwasome)

style = com.staticFile('src/style.css')

@com.main(css=style)
def app():
    return {
            "routes":            
                    {
                        "/": 
                            [
                                Nav(),
                            ],
                        "title":'ola mundo'
                    }
            }