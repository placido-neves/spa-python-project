from bs4 import BeautifulSoup, Comment
from dom.render import JS
from dom.CDN import AddCDN

add = AddCDN()
js = JS()

get_js = js.getComponets()



def inject_live_server_script(path):
    with open(path) as fp:
        soup = BeautifulSoup(fp, features='html.parser')
        head = soup.find('head')
        body =  soup.find('body')
        if head is None:
            head_tag = soup.new_tag('head')
            soup.append(head_tag)
            head = soup.find('head')
        for cdn in add.get_link():
            news_tag = soup.new_tag(name='link',attrs={"rel":'stylesheet',"type":"text/css","href":cdn})
            head.append(news_tag)

        for n in list(get_js):
            new_script = soup.new_tag(name='script', attrs={'src': n})
            body.append(new_script)
        
      
        return soup.encode()