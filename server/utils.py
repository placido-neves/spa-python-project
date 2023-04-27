import socket
import os

root_path = os.path.dirname(os.path.dirname(__file__))


def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("localhost", port)) == 0


  
       