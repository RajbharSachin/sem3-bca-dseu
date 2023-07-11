import socket 
import threading

HOST = '127.0.0.1' # private ip adddress here (cmd ipconfig or myip.is)
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # internet & tcp sockets
server.bind((HOST, PORT))

server.listen()   # acts as host
clients = []      # used for communication
nicknames = []

# broadcast the message
def broadcast(message):
    for client in clients:
        client.send(message)

# handle (individual connections)
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            print(f"{nicknames[clients.index(client)]}") # lock the message It TO BE PRINTED ON SERVER CONSOLE
            broadcast(message)                           # f means formatted string 
        except:   # if disconnects remove from clients or nicknames list
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            break #thread stops

# recieve the message
def receive():
    while True:
        client, address = server.accept() #add new clients
        print(f"Connected with {str(address)}!")

        client.send("NICK".encode('utf-8')) # using nickname
        nickname = client.recv(1024)

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} connected to the server!\n".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        #connection with each client
        thread = threading.Thread(target=handle, args=(client,))  # , means tuple
        thread.start()

print("!Server Running..")
receive()