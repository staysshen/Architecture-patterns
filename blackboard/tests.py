import unittest
from blackboard import Blackboard, ImageRecognitionResource, ImageRecognitionController


class BlackboardTest(unittest.TestCase):
    def test_image_recognition(self):
        # Arrange
        blackboard = Blackboard()
        image = "path/to/image.jpg"
        blackboard.add_data("image", image)

        image_resource = ImageRecognitionResource(blackboard)
        controller = ImageRecognitionController(blackboard)

        # Act
        image_resource.update_blackboard()
        controller.update_assets()

        # Assert
        labels = blackboard.get_data("labels")
        expected_labels = ["cat", "dog", "tree"]
        self.assertEqual(labels, expected_labels)


if __name__ == '__main__':
    unittest.main()
