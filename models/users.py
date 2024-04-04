from pydantic import BaseModel


class Users(BaseModel):
    name: str
    last_name: str
    username: str
    email: str
    password: str

