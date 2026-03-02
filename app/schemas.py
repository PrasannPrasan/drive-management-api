from pydantic import BaseModel, Field
from datetime import date, time
from typing import Optional


class DriveCreate(BaseModel):
    city: str
    location: str
    date: date
    time: time
    volunteers_required: int = Field(gt=0)
    description: Optional[str] = None


class DriveResponse(DriveCreate):
    id: int

    class Config:
        orm_mode = True