import socket
import threading

HOST = "127.0.0.1"  
PORT = 5000  

clients = []
nicknames = []

def run(message):# трансляция
    for client in clients:
        client.send(message)

def process(client):# обработка клиента
    while True:
        try:
            message = client.recv(1024)
            run(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            run(f'{nickname} left the chat!'.encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        while True:
            client, adress = server.accept()
            print(f"Connected with {str(adress)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            print(f'Nickname is {nickname}')
            run(f'{nickname} joined the chat!'.encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target=process, args = (client,))
            thread.start()

print('Server is listening...')
receive()


