import random
import sys
from socket import *

port = int(sys.argv[1])

server_socket = socket(AF_INET, SOCK_DGRAM)
# bind() is used to associate the socket with a specific network interface and port number
server_socket.bind(('', port))

while True:
    rand = random.randint(0, 10)
    # bufsize - The number of bytes to be read from the UDP socket.
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    if rand < 4:
        continue
    server_socket.sendto(message, address)

