import sys, time
from socket import *

argv = sys.argv
host = argv[1]
port = argv[2]
timeout = 1

cliente = socket(AF_INET, SOCK_DGRAM)
cliente.settimeout(timeout)

port = int(port)

aux_ping = 0

while aux_ping < 10:
    aux_ping += 1
    data = "[Ping " + str(aux_ping) + " " + time.asctime() + "]"
    try:
        time_send = time.time()
        data = data.encode()
        cliente.sendto(data, (host, port))
        message, address = cliente.recvfrom(1024)
        time_receive = time.time()
        print("Reply from " + address[0] + ": " + message.decode())
        print("RTT: " + str(time_receive - time_send))
    except:
        print("Request denied")
        continue

cliente.close()

print(argv)
