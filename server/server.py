from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
from server.inject import inject_live_server_script
from dom.render import  Render, Effect, JS
from dom.observer import subject, Observer
from requests import get
import email.utils
import datetime
import os
import json

js = JS()
effect = Effect()
get = js.getComponets()

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        url = urlparse(self.path)
        request_file_path = url.path.strip('/')

        for script in list(get.keys()):
            if script == request_file_path:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                self.send_response(200)
                self.end_headers
                json_loads = json.loads(body)
                if json_loads:
                    Observer(subject)
                    subject.change = json_loads
                self.wfile.write(bytes(json.dumps(effect.getComponets()),'utf-8'))


    def do_GET(self):
        url = urlparse(self.path)
        request_file_path = url.path.strip('/')

        if request_file_path == "api":
            render = Render()
            self.send_response(200)
            self.send_header('Content-type',"application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(render.getComponets()),'utf-8'))
 
        elif request_file_path == "index.js":
            self.send_response(200)
            self.send_header('Content-type',"application/javascript")
            self.end_headers()
            app = open('./app/index.js').read()
            self.wfile.write(bytes(app,'utf-8'))

        elif not os.path.exists(request_file_path):
            '''fs = os.stat('./app/index.html')
            test = [True]

            if('If-Modified-Since' in self.headers and "If-None-Match" not in self.headers):
                ims = email.utils.parsedate_to_datetime(self.headers('IF-Modified-Since'))
                if ims.tzinfo is None:
                    ims = ims.replace(izifo=datetime.timezone.utc)
                if ims.tzinfo is datetime.timezone.utc:
                    last_modif = datetime.datetime.fromtimestamp(fs.st_mtime, datetime.timezone.utc)
                    if last_modif <=ims:
                        test[0]=False
       # if not test[0]:
       #     self.send_response(304)
        #else:
        self.send_header('Last-Modified',self.date_time_string(fs.st_mtime))'''
            self.send_response(200)    
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(inject_live_server_script('./app/index.html'))


