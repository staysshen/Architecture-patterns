import unittest
from filter import UppercaseFilter, ReverseFilter, Pipe


class FilterTestCase(unittest.TestCase):
    def test_uppercase_filter(self):
        data = "hello"
        expected_result = "HELLO"
        filter = UppercaseFilter()
        result = filter.process(data)
        self.assertEqual(result, expected_result)

    def test_reverse_filter(self):
        data = "hello"
        expected_result = "olleh"
        filter = ReverseFilter()
        result = filter.process(data)
        self.assertEqual(result, expected_result)

    def test_pipe_with_filters(self):
        data = "hello"
        expected_result = "OLLEH"
        pipe = Pipe()
        pipe.add_filter(UppercaseFilter())
        pipe.add_filter(ReverseFilter())
        result = pipe.process_data(data)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
