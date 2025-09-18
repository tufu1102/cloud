import socket 

import pickle

class DataObject:

    def __init__(self,name,values):
        self.name = name
        self.values = values

dataob = DataObject('Jash',[100,100,100])

client_side = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_side.connect(('localhost',8000))

msg = pickle.dumps(dataob)
client_side.sendall(msg)
data = client_side.recv(1024).decode()

print(f"total = {data}")

client_side.close()