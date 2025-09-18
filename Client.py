import socket

client_side = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'
port = 8000

client_side.connect((host,port))

msg = input("Enter the message:")
client_side.send(msg.encode())
data = client_side.recv(1024).decode()
print(f"Server: {data}")

client_side.close()
