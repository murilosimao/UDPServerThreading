from threading import Thread
import time
from socket import *

class Server:
    def __init__(self):
        self.server_port = 12000
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(('', self.server_port))
        self.clients_list = []

    def circle_area(self, radius, client_address):
        result = 3.14 * int(radius)**2
        self.sock.sendto(bytes(str(result), "utf-8"), client_address)
    
    def listen_clients(self):
        while True:
            message , client_address = self.sock.recvfrom(2048)
            t = Thread(target=self.circle_area, args=(message, client_address))
            t.start()

if __name__ == "__main__":
    server = Server()
    server.listen_clients()