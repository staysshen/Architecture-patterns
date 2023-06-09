import unittest
from master import Master
from slave import Slave

class MasterSlaveTest(unittest.TestCase):
    def test_master_slave(self):
        # Arrange
        master = Master()
        slave1 = Slave()
        slave2 = Slave()
        master.add_slave(slave1)
        master.add_slave(slave2)

        request = "Sample Request"

        # Act
        results = master.process_request(request)

        # Assert
        self.assertEqual(len(results), 2)
        self.assertEqual(results[0], f"Processing request '{request}' in slave.")
        self.assertEqual(results[1], f"Processing request '{request}' in slave.")

if __name__ == '__main__':
    unittest.main()
