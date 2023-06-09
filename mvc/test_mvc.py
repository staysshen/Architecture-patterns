import unittest
from model import User
from view import UserView
from controller import UserController

class MVCTest(unittest.TestCase):
    def test_mvc(self):
        # Arrange
        user = User("John Doe", "johndoe@example.com")
        view = UserView()
        controller = UserController(user, view)

        # Act
        controller.update_view()

        # Act
        controller.set_user_name("Jane Smith")
        controller.set_user_email("janesmith@example.com")
        controller.update_view()

        # Assert
        # Again, check the console output to verify that the updated user information is displayed correctly.

if __name__ == '__main__':
    unittest.main()
