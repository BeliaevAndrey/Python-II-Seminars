# Доработайте классы исключения так, чтобы они выдали подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода проекта.

from s13_t04_User_class import forming_fun, User
from s13_t03_Custom_Exceptions import AccessError, LevelError

ALLOWED_LEVEL = 5


class TaskFive:
    """
    The class provides "entrance" to somewhere... That's all the point.
    Checks input data; raises exceptions.
    """

    def __init__(self, file_name: str, access_level) -> None:
        self.users_set = forming_fun(file_name)
        self.authorized = set()
        self.access_level = access_level

    @staticmethod
    def scan_uid_uname():
        while True:
            try:
                u_id = int(input('input user ID: '))
                break
            except ValueError as exc:
                print(f'{exc.__class__.__name__} {exc}      -- Integers only!')
        u_name = input('input user Name: ')
        return u_id, u_name

    def entrance(self, u_id: int = -1, u_name: str = ''):
        stub_level = 0      # rough crutch
        if not u_name or u_id == -1:
            u_id, u_name = self.scan_uid_uname()
        tmp_user = User('0', str(u_id), u_name)
        if tmp_user not in self.users_set:
            raise AccessError(u_id=u_id, u_name=u_name)
        for i_user in self.users_set:
            if i_user == tmp_user and (stub_level := i_user.acs_level) >= self.access_level:
                self.authorized.add(i_user)
                break
        else:
            raise LevelError(lvl_needed=self.access_level, lvl_given=stub_level)

    def get_authorized(self) -> set[User]:
        return self.authorized


if __name__ == '__main__':
    # print('just a module now')
    fun1 = TaskFive('index.json', 5)
    fun1.entrance(123456, "name 000")
    print(fun1.get_authorized())
