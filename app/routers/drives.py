from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date

from ..database import SessionLocal
from ..models import Drive
from ..schemas import DriveCreate, DriveResponse

router = APIRouter(
    prefix="/drives",
    tags=["Drives"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DriveResponse, status_code=201)
def create_drive(drive: DriveCreate, db: Session = Depends(get_db)):
    if drive.date < date.today():
        raise HTTPException(status_code=400, detail="Date cannot be in the past")

    new_drive = Drive(**drive.dict())
    db.add(new_drive)
    db.commit()
    db.refresh(new_drive)
    return new_drive


@router.get("/", response_model=list[DriveResponse])
def get_drives(
    city: str = Query(...),
    db: Session = Depends(get_db),
):
    drives = db.query(Drive).filter(Drive.city.ilike(city)).all()
    return drives