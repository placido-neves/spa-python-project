from http.server import HTTPServer
from server.server import Handler
from server.utils import is_port_in_use
from dom.render import Render
from src.app import app
import json

port = 3000

render = Render()
render.setComponents(json.dumps(app()))


while is_port_in_use(3000):
    port += 1
    print(port)
    
httpd = HTTPServer(('localhost',port),Handler)

print(f'cli service started at http://localhost:{port}')

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print('server close')