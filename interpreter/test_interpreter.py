import unittest
from interpreter import *


class InterpreterTest(unittest.TestCase):
    def test_expression_evaluation(self):
        # Arrange
        context = Context()
        context.set_variable("A", 5)
        context.set_variable("B", 10)

        expression = build_expression_tree()

        # Act
        result = evaluate_expression(expression)

        # Assert
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
