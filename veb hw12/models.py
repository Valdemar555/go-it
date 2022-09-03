from sqlalchemy import Column, Integer, String, Date
from db.db import Base, engine, db_session

class BoxingResults(Base):
    __tablename__ = "boxing_results"
    id = Column(Integer, primary_key=True)
    vs = Column(String(100), nullable=False)
    result = Column(String(10), nullable=False)
    
class InternationalMatches(Base):
    __tablename__ = "international"
    id = Column(Integer, primary_key=True)
    f_match = Column(String(80), nullable=False)
    score = Column(String(10), nullable=True)


if __name__ == "__main__":
    Base.metadata.create_all(engine)