import server.database.users

from ..boundary import log
from ..database.users import types, users

EMPTY_USER = types.UserIn(id=0, username="empty", password="", name="empty")

@log.try_except(message="user not found", default=EMPTY_USER)
def find_user_info(userin: types.UserIn) -> types.UserIn:
    return next([user for user in users.load() if user.verify_user(userin)])
