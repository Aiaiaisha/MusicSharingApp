import socket
from threading import Thread

IP_ADD = "127.0.0.1"
PORT = 8080
SERVER = None
BUFFER_SIZE = None
clients = {}

def acceptConnections():
    global SERVER
    global clients

    while True:
        client,add = SERVER.accept()
        print(client,add)

def setup():
    global SERVER
    global IP_ADD
    global PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind(IP_ADD,PORT)
    SERVER.listen()

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    acceptConnections()

setup_thread = Thread(target = setup)
setup_thread.start()