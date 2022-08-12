from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person, Record
from datetime import date

engine = create_engine("sqlite:///contact_book.db")
Session = sessionmaker(bind=engine)
session = Session()

person1 = Person(first_name="Taras", last_name="Shevchenko")
person2 = Person(first_name="Ivan", last_name="Franko")

record1 = Record(
    first_phone="0997776655",
    second_phone="0937776655",
    email="taras1814@gmail.com",
    birthday=date(day=9, month=3, year=1991),
    address="Kaniv",
    person=person1,
)
record2 = Record(
    person=person2,
    first_phone="0985588844",
    second_phone="0739944477",
    email="franko1856@gmail.com",
    birthday=date(day=2, month=6, year=1996),
    address="Lviv",
)

session.add(record1)
session.add(record2)

session.commit()
session.close()
