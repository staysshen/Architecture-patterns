import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []
        self.is_running = False

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"Peer listening on {self.host}:{self.port}")

        self.is_running = True
        while self.is_running:
            conn, addr = self.socket.accept()
            self.handle_connection(conn)

    def handle_connection(self, conn):
        self.connections.append(conn)
        print(f"New connection: {conn.getpeername()}")
        
        # Start a new thread to handle communication with the connected peer
        threading.Thread(target=self.receive_data, args=(conn,)).start()

    def receive_data(self, conn):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data from {conn.getpeername()}: {data.decode()}")

    def send_data(self, peer, data):
        try:
            conn = socket.create_connection(peer)
            conn.sendall(data.encode())
            conn.close()
        except ConnectionRefusedError:
            print(f"Unable to connect to {peer[0]}:{peer[1]}")

    def stop(self):
        self.is_running = False
        self.socket.close()
        for conn in self.connections:
            conn.close()

