import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('localhost',8080))
while True:

        request = input('> ')
        client.send(request.encode())
        response = client.recv(1024).decode()
        print(response)

        client.close()

