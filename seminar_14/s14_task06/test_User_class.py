# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
import pytest

from s13_t04_User_class import User
from s13_t03_Custom_Exceptions import *
from sem13_task06 import TaskFive, forming_fun




if __name__ == '__main__':
    pytest.main(['-v'])
