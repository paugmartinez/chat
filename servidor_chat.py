import socket

PORT = 8093
IP = "127.0.0.1"
MAX_OPEN_REQUESTS = 5



def process_client(clientsocket):
    print(clientsocket)
    condition = True
    while condition:
        inbox = clientsocket.recv(2048).decode("utf-8")
        print("El cliente nos dice: ", inbox)
        if inbox.lower() == "salir":
            print("saliendo por parte del cliente")
            condition = False

        out = input("Introduzca un mensaje (nos dice el servidor): ")
        outbox = str.encode(out)
        clientsocket.send(outbox)
        if out.lower() == "salir" :
            print("saliendo")
            condition = False

    clientsocket.close()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = IP
try:
    serversocket.bind((hostname, PORT))
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        print("Esperando conexión con %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
