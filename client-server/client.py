import socket

class Client:
    def send_request(self, host, port, request):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(request.encode())
            response = client_socket.recv(1024).decode()
        
        return response
