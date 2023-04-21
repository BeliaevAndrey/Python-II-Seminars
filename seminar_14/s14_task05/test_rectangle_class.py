import unittest
from unittest.mock import patch
import io

from s11_t06_Rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):

    def setUp(self) -> None:
        self.tested_rectangle = Rectangle(20, 10)

    def test_perimeter(self):
        self.assertEqual((20 + 10) * 2, self.tested_rectangle.get_perimeter())

    def test_area(self):
        self.assertEqual(20 * 10, self.tested_rectangle.get_area())

    def test_eq(self):
        self.assertTrue(Rectangle(10, 20) == self.tested_rectangle)

    def test_gt(self):
        self.assertTrue(Rectangle(20) > self.tested_rectangle)

    def test_lt(self):
        self.assertTrue(Rectangle(19, 10) < self.tested_rectangle)

    def test_ne(self):
        self.assertTrue(Rectangle(19, 10) != self.tested_rectangle)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error(self, mock_stdout):
        self.assertRaises(TypeError, self.tested_rectangle.__eq__,  10)
        self.assertEqual("Not a 'Rectangle' instance", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
