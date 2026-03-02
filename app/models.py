from sqlalchemy import Column, Integer, String, Date, Time, Text
from .database import Base


class Drive(Base):
    __tablename__ = "drives"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, nullable=False, index=True)
    location = Column(String, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    volunteers_required = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)