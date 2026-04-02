from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.services.user_service import create_user, authenticate_user
from app.core.security import create_access_token
from app.api.deps import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user.username, user.password)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.username})
    return {"access_token": token}