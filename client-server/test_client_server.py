import unittest
from server import Server
from client import Client
import threading

class ClientServerTest(unittest.TestCase):
    def test_client_server_interaction(self):
        # Arrange
        host = '127.0.0.1'
        port = 12345

        server = Server(host, port)
        server_thread = threading.Thread(target=server.start)
        server_thread.daemon = True
        server_thread.start()

        client = Client()

        # Act
        request = "Hello, server!"
        response = client.send_request(host, port, request)

        # Assert
        expected_response = "Server response to 'Hello, server!'"
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
