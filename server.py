import socket
import threading

# The following variables are constants
HEADER = 128  # Will contain information about message properties
PORT = 1996  # Port that the socket will be using
HOST_NAME = socket.gethostname()  # will get the name of the machine
# will get the IP address by using the machine name
SERVER = socket.gethostbyname(HOST_NAME)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))  # passed as tuple


def Init():  # this function will be called to initilize the server
    server.listen()
    print("Server is listening on " + SERVER)


print("initializing server...")
Init()
