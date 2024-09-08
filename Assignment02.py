import socket
HOST = '127.0.0.1'
PORT = 6060
C_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
C_Socket.connect((HOST, PORT))
x = 0
while x<3: 
    message = input("\nEnter the message: ")
    C_Socket.send(message.encode())
    msg_recvd = C_Socket.recv(1024)
    print('Total Character Counts: ',msg_recvd.decode('utf-8'))
    msg_recvd = C_Socket.recv(1024)
    print('Message: ',msg_recvd.decode('utf-8'))
    x+=1
C_Socket.close()