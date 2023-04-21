import pytest

from sem14_task04 import symbol_deleter


def test_no_changed():
    assert ("first test string" == symbol_deleter("first test string"))


def test_no_upper_case():
    assert ("second test string" == symbol_deleter("second test string".title()))


def test_no_punctuation():
    assert ("third punctuation test string " == symbol_deleter("Third punctuation test string [,.;:|\\/!'\"]"))


def test_latin_only():
    assert ("   and this is to be kept" == symbol_deleter('Это надо удалить! And this is to be kept.'))


def test_all_together():
    assert ('this text has to be saved     ',
            symbol_deleter('This text has to be saved. А этот удален 1234098765!'
                           '"№;%%::??**(()()(* ?:%:%;;!@#$%^&*(*)_+=}{[]|\\/?.,<>`~'))


def test_error(capfd):
    with pytest.raises(TypeError, match="Argument is to be a string"):
        symbol_deleter(100)


if __name__ == '__main__':
    pytest.main(['-v'])
