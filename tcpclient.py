import socket

socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

socket_client.connect(('127.0.0.1',1234))

print('Connected to the server ',socket_client.getsockname())

msg=""

while msg!="bye":
    msg=input("Enter msg to server:")
    socket_client.send(msg.encode())
    server=socket_client.recv(1024)
    print("Recieved from server:",server.decode())
socket_client.close()
     
