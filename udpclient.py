import socket

client=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg=""
while msg!='bye':
    msg=input("Enter your message:")
    encoded=str.encode(msg)
    client.sendto(encoded,('127.0.0.1',1234))
    if msg=='bye':
        break
    server_msg=client.recvfrom(1024)
    print(f"Server:{server_msg[0].decode()}")
print("Client shut down!")