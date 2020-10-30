import socket
import threading

# The following variables are constants
HEADER = 64  # Will contain information about message properties
PORT = 5050  # Port that the socket will be using
HOST_NAME = socket.gethostname()  # will get the name of the machine
# will get the IP address by using the machine name
SERVER = socket.gethostbyname(HOST_NAME)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))  # passed as tuple
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disconnect"


def Init():  # this function will be called to initilize the server
    server.listen()
    print("Job Creator is listening on " + SERVER)
    while True:  # server will always be listening
        # will wait for a connection and store address in addr and a socket object in conn
        conn, addr = server.accept()
        # will start a thread where the function ClientHandler will be used to handle the upcoming connection.
        thread = threading.Thread(target=ClientHandler, args=(conn, addr))
        thread.start()

        # will display all active threads, we are subtracting 1 since we will always have 1 active thread at minimum even without connections
        print(f"THE NUMBER OF ACTIVE CONNECTIONS IS CURRENTLY  {threading.active_count() - 1}")


def ClientHandler(addr, conn):
    print(addr + "has connected.")
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_length: #will ignore any messages with are 0, usually connection a 0 message is sent
            msg_length = int(msg_length)
            # code will stop here until a msg is received from the client, it will receive a HEADER number of bytes and it will decode the message from its bytes format to a string.
            msg_len = int(msg_len)  # convert message length to an int
            msg = conn.recv(msg_len).deco8de(FORMAT)
            # displays message
            print(addr + " has sent the following message: " + msg)
            if msg == DISCONNECT_MSG:  # if client asks to disconnect it will disconnect
                connected = False

    conn.close()


print("initializing server...")
Init()
