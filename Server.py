import socket

server_side = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = 'localhost'

port = 8000

server_side.bind((host,port))

server_side.listen(1)

print(f"you are listening to the port {port}")

conn,addr = server_side.accept()

print(f"yeah buddy you are connected to {addr}")

data = conn.recv(1024).decode()
print(f"Client: {data}")

response = "Welcome back to the field buddy"

conn.send(response.encode())

conn.close()
