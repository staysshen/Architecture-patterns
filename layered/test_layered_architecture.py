import unittest
from presentation_layer import PresentationLayer
from application_layer import ApplicationLayer
from data_layer import DataLayer

class LayeredArchitectureTest(unittest.TestCase):
    def test_layered_architecture(self):
        # Arrange
        database = MockDatabase()  # Replace with a real database implementation
        data_layer = DataLayer(database)
        application_layer = ApplicationLayer(data_layer)
        presentation_layer = PresentationLayer(application_layer)

        request = "Sample Request"

        # Act
        response = presentation_layer.process_request(request)

        # Assert
        self.assertEqual(response, "Processed Response")

if __name__ == '__main__':
    unittest.main()
