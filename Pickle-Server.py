import socket

import pickle

class DataObject:

    def __init__(self,name,values):
        self.name = name
        self.values = values

server_side = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_side.bind(('localhost',8000))
server_side.listen(2)
print(f"server is listening to port")
while True:
    conn,addr = server_side.accept()
    print(f"client connected with the {addr}")
    data = conn.recv(1024)
    if not data:
        conn.close()
        continue
    obj = pickle.loads(data)
    total = sum(obj.values)

    print(f"total is {total}")

    conn.send(str(total).encode())
    conn.close()
