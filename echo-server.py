import socket
import threading

#AF_NET = IPv4
#SOCK_STREAM = TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind the socket to port 10000 at IP address 0.0.0.0
sock.bind(('0.0.0.0', 10000))

#Allow the socket to listen for at most 1 connection 
sock.listen(1)

#List of connections
connections = []

def handler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True #Program able to exit regardless if there are any threads still running
    cThread.start()
    connections.append(c)
    print(len(connections),"connection:",connections) if len(connections) == 1 else print(len(connections),"connections:",connections)
