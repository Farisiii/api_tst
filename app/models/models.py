from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List
from datetime import datetime

class TimeSlot(BaseModel):
    start: str
    end: str
    
    @field_validator('start', 'end')
    def validate_time_format(cls, v):
        try:
            datetime.strptime(v, "%H:%M")
            return v
        except ValueError:
            raise ValueError("Time must be in HH:MM format")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "start": "09:00",
                "end": "09:30"
            }
        }
    }

class Availability(BaseModel):
    date: str
    slots: List[TimeSlot]
    
    @field_validator('date')
    def validate_date_format(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
            return v
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "date": "2024-01-01",
                "slots": [
                    {"start": "09:00", "end": "09:30"},
                    {"start": "10:00", "end": "10:30"}
                ]
            }
        }
    }

class Provider(BaseModel):
    id: int
    name: str
    image: str
    rating: float = Field(..., ge=0, le=5)
    reviews: int = Field(..., ge=0)
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "name": "John Doe",
                "image": "provider_1.jpg",
                "rating": 4.5,
                "reviews": 100
            }
        }
    }

class Service(BaseModel):
    id: int
    type: str
    provider: Provider
    rate: float = Field(..., gt=0)
    availability: List[Availability]
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "id": 1,
                "type": "Massage",
                "provider": {
                    "id": 1,
                    "name": "John Doe",
                    "image": "provider_1.jpg",
                    "rating": 4.5,
                    "reviews": 100
                },
                "rate": 50.0,
                "availability": [
                    {
                        "date": "2024-01-01",
                        "slots": [
                            {"start": "09:00", "end": "09:30"},
                            {"start": "10:00", "end": "10:30"}
                        ]
                    }
                ]
            }
        }
    }