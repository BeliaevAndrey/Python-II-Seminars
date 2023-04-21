import unittest
from unittest.mock import patch
import io

from sem14_task03 import symbol_deleter


class TestSymbolDeleter(unittest.TestCase):

    def test_no_changed(self):
        self.assertEqual("first test string", symbol_deleter("first test string"))

    def test_no_upper_case(self):
        self.assertEqual("second test string", symbol_deleter("second test string".title()))

    def test_no_punctuation(self):
        self.assertEqual("third punctuation test string ", symbol_deleter("Third punctuation test string [,.;:|\\/!'"))

    def test_latin_only(self):
        self.assertEqual("   and this is tobe kept", symbol_deleter('Это надо удалить! And this is tobe kept.'))

    def test_all_together(self):
        self.assertEqual('this text has to be saved     ',
                         symbol_deleter('This text has to be saved. А этот удален 1234098765!'
                                        '"№;%%::??**(()()(* ?:%:%;;!@#$%^&*(*)_+=}{[]|\\/?.,<>`~'))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error(self, mock_stdout):
        self.assertRaises(TypeError, symbol_deleter, 0)
        self.assertEqual("Argument is to be a string\n",
                         mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main(verbosity=2)
