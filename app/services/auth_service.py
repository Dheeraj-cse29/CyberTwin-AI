from datetime import timedelta

from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
)


def register_user(db: Session, user_data):

    existing_user = db.query(User).filter(
        User.username == user_data.username
    ).first()

    if existing_user:
        return None

    new_user = User(
        full_name=user_data.full_name,
        email=user_data.email,
        username=user_data.username,
        password=hash_password(user_data.password),
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(
    db: Session,
    username: str,
    password: str
):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if user is None:
        return None

    if not verify_password(
        password,
        user.password
    ):
        return None

    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role,
        },
        expires_delta=timedelta(minutes=30),
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }