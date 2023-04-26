import json


class User:
    """Carries data on user"""

    def __init__(self, acs_level: str, u_id: str, u_name: str) -> None:
        """
        init method
        :param acs_level: str   -- a user access level (numeric), type str because data is read from json-file
        :param u_id: str        -- a user id (numeric), type str because data is read from json-file
        :param u_name: str      -- a username
        """
        self.acs_level = int(acs_level)
        self.u_id = int(u_id)
        self.u_name = u_name

    def __str__(self):
        return f'UID: {self.u_id}; Name: {self.u_name}; level: {self.acs_level} '

    def __repr__(self):
        return f'User(acs_level={self.acs_level}, u_id={self.u_id}, u_name={self.u_name})'

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise ValueError('Wrong type')
        return self.u_id == other.u_id and self.u_name == other.u_name

    def __hash__(self):
        return hash(self.u_name) + hash(self.u_id)


def forming_fun(file_name: str) -> set[User]:
    with open(file_name, 'r', encoding='utf-8') as f_in:
        users_dct = json.load(f_in)
    users_set = set()
    for acs_lvl, user_dct in users_dct.items():
        for u_id, u_name in user_dct.items():
            users_set.add(User(acs_lvl, u_id, u_name))
    return users_set


if __name__ == '__main__':
    print('Just a module now')
