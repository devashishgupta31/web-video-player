from ...boundary import files
from . import types

PATH = "../temp/users.json"


def load() -> list[types.UserIn]:
    return types.Schema(**files.get_json(PATH)).data

def get_users() -> list[types.UserOut]:
    return [user.get_user() for user in load()]
