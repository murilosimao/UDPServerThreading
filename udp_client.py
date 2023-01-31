from socket import *

server_name = 'localhost'
server_port = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
message = input('Digite um numero: ')
client_socket.sendto(bytes(message, "utf-8"),(server_name, server_port))
answer, server_address = client_socket.recvfrom(2048)
print(answer.decode('utf-8'))
client_socket.close()