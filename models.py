# Models
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    lat = Column(Float)
    lng = Column(Float)

    universities = relationship("University", back_populates="location")

class University(Base):
    __tablename__ = "universities"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    location_id = Column(Integer, ForeignKey("locations.id"))
    
    location = relationship("Location", back_populates="universities")
    users = relationship("User", back_populates="university")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    linkedin = Column(String, unique=True, nullable=False)
    instagram = Column(String, unique=True)

    description = Column(String)
    university_id = Column(Integer, ForeignKey("universities.id"))
    university = relationship("University", back_populates="users")

