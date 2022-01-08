
from passlib.hash import bcrypt
from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    name: str
    username: str


class UserIn(UserOut):
    password: str

    def get_user(self) -> UserOut:
        return UserOut(**self.json(exclude={"password"}))

    def verify_user(self, user) -> bool:
        return self.username == user.username and self.verify_password(user.password)

    def verify_password(self, password) -> bool:
        return bcrypt.verify(password, self.password)

class Schema(BaseModel):
    data: list[UserIn]
