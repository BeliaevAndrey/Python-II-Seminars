# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import pytest

from s13_t04_User_class import User
from s13_t03_Custom_Exceptions import *
from sem13_task06 import TaskFive, forming_fun


@pytest.fixture()
def set_up():
    return TaskFive('index.json', 5)


def test_access_fail(set_up):
    with pytest.raises(AccessError, match='Access Denied'):
        set_up.entrance(1234, "asdfgh")


def test_success(set_up):
    set_up.entrance(123456, "name 000")
    assert {User('6', '123456', 'name 000')} == set_up.get_authorized()


def test_entrance_fail(set_up):
    with pytest.raises(LevelError, match='Wrong Level'):
        set_up.entrance(125, "name 2")


if __name__ == '__main__':
    pytest.main(['-v'])
