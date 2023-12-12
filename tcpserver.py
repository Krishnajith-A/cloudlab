import socket
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',1234))
print("Server on at ",server_socket.getsockname())
server_socket.listen()
stat=True
while stat==True:
    print("Waiting for a connection....")
    conn, addr=server_socket.accept()
    client=''
    data=''
    while data!='bye':
        data=conn.recv(1024)
        if not data:
            break
        client=data.decode('utf8')
        print('Client:',client)
        msg=input("Enter server message:")
        conn.send(msg.encode())
        client=''
    conn.close()
    s=input("Y/N:")
    if s=='y' or s=='Y':
        stat=True
    else:
        stat=False
print('Client disconnected')