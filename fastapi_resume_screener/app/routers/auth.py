from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models, auth, database
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=schemas.UserOut)
async def signup(user: schemas.UserCreate, session: AsyncSession = Depends(database.get_session)):
    existing = await session.execute(models.User.__table__.select().where(models.User.email == user.email))
    if existing.scalar():
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = auth.hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_pw, full_name=user.full_name)
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(database.get_session)):
    query = await session.execute(models.User.__table__.select().where(models.User.email == form_data.username))
    user = query.scalar_one_or_none()
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
