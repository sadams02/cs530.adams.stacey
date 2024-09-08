import socket
HOST = '127.0.0.1'
PORT = 6060
print("Server running...")  
S_Socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
S_Socket.bind((HOST, PORT))
S_Socket.listen(1)
client_Added, client_Address = S_Socket.accept()
print("Connection recieved from: ",str(client_Address))
message = client_Added.recv(1024)
while message:
    recvd_msg = message.decode('utf-8')
    char_count = len(recvd_msg)
    print('Received From Client:' ,recvd_msg)
    msg_send = str(char_count)
    client_Added.send(msg_send.encode('utf-8'))
    msg_send = recvd_msg.upper()
    client_Added.send(msg_send.encode('utf-8'))
    message = client_Added.recv(1024)  
client_Added.close()
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


