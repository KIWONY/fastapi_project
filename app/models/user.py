from pydantic import BaseModel, EmailStr


class UserResponse(BaseModel):
    email: EmailStr
    password: str | None = None
    username: str

    class Config:
        orm_mode = True
