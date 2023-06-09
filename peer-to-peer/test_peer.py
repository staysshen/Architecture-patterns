import unittest
import threading
from peer import Peer

class PeerTest(unittest.TestCase):
    def test_peer_communication(self):
        # Arrange
        host = 'localhost'
        port1 = 5000
        port2 = 6000
        peer1 = Peer(host, port1)
        peer2 = Peer(host, port2)

        def start_peer(peer):
            peer.start()

        # Act
        threading.Thread(target=start_peer, args=(peer1,)).start()
        threading.Thread(target=start_peer, args=(peer2,)).start()

        # Wait for the peers to start
        threading.Event().wait(1)

        peer1.send_data((host, port2), "Hello from Peer 1!")
        peer2.send_data((host, port1), "Hello from Peer 2!")

        # Wait for the messages to be received
        threading.Event().wait(1)

        # Assert
        self.assertEqual(len(peer1.connections), 1)
        self.assertEqual(len(peer2.connections), 1)

    def tearDown(self):
        peer1.stop()
        peer2.stop()

if __name__ == '__main__':
    unittest.main()
