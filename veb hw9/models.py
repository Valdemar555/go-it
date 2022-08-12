from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, Column, Integer, String, Date

Base = declarative_base()

class Person(Base):

    __tablename__ = "person"
    id = Column(Integer, primary_key= True)
    first_name = Column(String(50), nullable = False)
    last_name = Column(String(50), nullable = False)

    record = relationship("Record", cascade="all, delete", back_populates="person")


class Record(Base):

    __tablename__ = "record"
    record_id = Column(Integer, primary_key=True)
    first_phone = Column(String(15), nullable=False)
    second_phone = Column(String(15), nullable=True)
    email = Column(String(15), nullable=True)
    birthday = Column(Date, nullable=True)
    address =  Column(String(50), nullable=True)
    person_id = Column(Integer, ForeignKey(Person.id, ondelete="CASCADE"))

    person = relationship("Person", cascade="all, delete", back_populates="record")