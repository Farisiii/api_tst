from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "password": "strongpassword123"
            }
        }
    }

class UserRegister(UserLogin):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
                "token_type": "bearer",
                "expires_in": 86400
            }
        }
    }

class User(BaseModel):
    email: EmailStr
    role: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "email": "user@example.com",
                "role": "user"
            }
        }
    }

class MessageResponse(BaseModel):
    message: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Operation successful"
            }
        }
    }