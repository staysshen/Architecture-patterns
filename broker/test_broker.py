import unittest
from broker import Broker, Request
from client import Client
from server_a import ServerA
from server_b import ServerB


class BrokerTest(unittest.TestCase):
    def test_broker_pattern(self):
        # Arrange
        broker = Broker()
        server_a = ServerA("ServerA")
        server_b = ServerB("ServerB")
        broker.register_server(server_a)
        broker.register_server(server_b)

        client = Client(broker)

        # Act
        request_data = "Hello, Broker!"
        response = client.send_request("ServerA", request_data)

        # Assert
        expected_result = "ServerA processed: Hello, Broker!"
        self.assertEqual(response.result, expected_result)

if __name__ == '__main__':
    unittest.main()
