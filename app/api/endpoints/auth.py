from fastapi import APIRouter, HTTPException
from app.core.security import create_access_token, verify_password, get_password_hash
from app.models.user import UserRegister, UserLogin, Token, MessageResponse
from app.db.fake_db import users_db

router = APIRouter()

@router.post("/register", response_model=MessageResponse)
async def register(user_data: UserRegister):
    """
    Register a new user account.
    """
    if user_data.email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    
    users_db[user_data.email] = {
        "password": get_password_hash(user_data.password),
        "role": "user"
    }
    
    return MessageResponse(message="User registered successfully")

@router.post("/login", response_model=Token)
async def login(user_data: UserLogin):
    """
    Login to get access token.
    """
    if user_data.email not in users_db:
        raise HTTPException(status_code=401, detail="User not found")
    
    user = users_db[user_data.email]
    
    if not verify_password(user_data.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token_data = {
        "email": user_data.email,
        "role": user["role"]
    }
    
    access_token = create_access_token(token_data)
    
    return Token(
        access_token=access_token,
        expires_in=24 * 3600
    )