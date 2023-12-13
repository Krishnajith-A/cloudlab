import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(('127.0.0.1',1234))

print("Listening....")

server_msg="Hello client"
encoded=str.encode(server_msg)

stat=True

while stat==True:
    byte_address_pair=server.recvfrom(1024)
    print("Connection established")
    msg=byte_address_pair[0].decode()
    address=byte_address_pair[1]
    print(f"Client IP address:{address}")
    print(f'Client Message:{msg}')
    while msg!='bye':
        encoded=str.encode(input("Enter server message:"))
        server.sendto(encoded,address)
        byte_address_pair=server.recvfrom(1024)
        msg=byte_address_pair[0]
        decoded=msg.decode()
        print(f"Client: {decoded}")
    stat=input("Should we wait for morem incoming messages:")
    if stat=='yes':
        stat=True
        print("waiting for new message")
    else:
        stat=False
        print("Server shutting down")
    