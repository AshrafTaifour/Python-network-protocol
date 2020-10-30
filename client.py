import socket #socket object will be used to make the connection
#CONSTANTS
HEADER = 64 # wILL BE THE HEADER LENGTH
PORT = 5050  # Port that the socket will be using
FORMAT = 'utf-8' #THIS WILL BE THE ENCODING FORMAT WHEN SENDING HEADER
DISCONNECT_MESSAGE = "!disconnect" #WHEN CLEINT DISCONNECTS OR TERMINATES CONNECTION
SERVER = "192.168.1.134" #NOTE THIS IS LOCAL IP ADDRESS ON LAN, PLEASE ADJUST IT TO THE SERVER IP ADDRESS BY RUNNING IPCONFIG ON WINDOWS
ADDR = (SERVER, PORT) #ADDRESS WILL BE TUPLE OF IP ADDRESS OF SERVER AND PORT#
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #CREATE NEW VARIABLE CALLED CLIENT AND MAKE IT AN OBJECT OF THIS CONNECTION
client.connect(ADDR) #CLIENT CONNECTS TO ABOVE IP ADDRESS

def send(msg): #DEFINED FUNCTION TO SEND MSG FROM CLIENT
    message = msg.encode(FORMAT) #TAKE MSG AND ENCOD IT
    msg_length = len(message) #GET LENGTH OF ENCODED MESSAGE 
    send_length = str(msg_length).encode(FORMAT) #SEND_length for header is equal to encoded message length
    send_length += b' ' * (HEADER - len(send_length)) #padd the message up to 124 bits adding b' ' byte of space 
    client.send(send_length) #send info to server first of the padded header message
    client.send(message) #send encoded message to server
    print(client.recv(2048).decode(FORMAT)) #print receive message from 


send("Hello World!") #first message to send
input()
send("Computer Network is fun!") # second message to send
input() # when user hits enter or any input it will now disconnect
send("Disconnecting now!") # disconnect message
send(DISCONNECT_MESSAGE) #send disconnect message
