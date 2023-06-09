import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()

            print(f"Server listening on {self.host}:{self.port}")

            while True:
                client_socket, client_address = server_socket.accept()
                print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

                request = client_socket.recv(1024).decode()
                response = self.process_request(request)
                client_socket.sendall(response.encode())

    def process_request(self, request):
        # Process the request and generate a response
        return f"Server response to '{request}'"
