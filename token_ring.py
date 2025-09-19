import socket
import threading
import time
import sys

# Define the circular order of token passing
NEXT_PORT = {
    5001: 5002,
    5002: 5003,
    5003: 5001,
}

def listen(my_port):
    """Listens for incoming TOKEN messages on the given port."""
    server = socket.socket()
    server.bind(('localhost', my_port))
    server.listen()
    print(f"[{my_port}] Listening...")

    while True:
        conn, _ = server.accept()
        msg = conn.recv(1024).decode()
        
        if msg == "TOKEN":
            print(f"[{my_port}] Received TOKEN.")
            enter_cs(my_port)
            send_token(NEXT_PORT[my_port])
        
        conn.close()

def enter_cs(my_port):
    """Simulates entering the critical section."""
    print(f"[{my_port}] Entering CS...")
    time.sleep(2)
    print(f"[{my_port}] Exiting CS.")

def send_token(next_port):
    """Sends the TOKEN to the next process in the ring."""
    time.sleep(1)
    s = socket.socket()
    s.connect(('localhost', next_port))
    s.send("TOKEN".encode())
    s.close()

def run(my_port, start_token=False):
    """Starts the listener thread and optionally starts the token."""
    threading.Thread(target=listen, args=(my_port,), daemon=True).start()
    
    if start_token:
        # Give others time to start
        time.sleep(2)
        send_token(my_port)

    # Keep the main thread alive
    while True:
        time.sleep(1)

if __name__ == "__main__":
    port = int(sys.argv[1])
    is_start = len(sys.argv) > 2 and sys.argv[2] == "start"
    run(port, is_start)
