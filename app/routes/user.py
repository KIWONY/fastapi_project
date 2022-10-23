
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status

from app.database.conn import db
from app.database.schema.user import User
from app.models.user import UserResponse

router = APIRouter()


@router.post("/users/register",status_code= status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user_data: UserResponse, db_session: Session = Depends(db.session)):
    db_user = User(email=user_data.email, password=user_data.password, username=user_data.username)
    db_session.add(db_user)
    db_session.commit()

    return db_user






