from models import Phone, Contacts, Record, Tag, Note
import connect
from datetime import date

phone1 = Phone(value="+380953335588")
phone2 = Phone(value="+380970008877")
phone3 = Phone(value="+380739995544")
phone4 = Phone(value="+380676655444")
phone5 = Phone(value="+380631112200")

contact1 = Contacts(first_name="Vitja", last_name="Volosok", phone=[phone1, phone2], birthday=date(year=1987, month=3, day=7), email="vitja@ukr.net", address="Chernigiv")
contact2 = Contacts(first_name="Lida", last_name="Fedorenko", phone=[phone3], birthday=date(year=1989, month=8, day=11), email="lida@ukr.net", address="Cherkasy")
contact3 = Contacts(first_name="Sasha", last_name="Makarenko", phone=[phone4], birthday=date(year=1986, month=3, day=8), email="makar@ukr.net", address="Kyiv")
contact4 = Contacts(first_name="Dima", last_name="Mozol", phone=[phone5], birthday=date(year=1991, month=5, day=13), email="mozol@ukr.net", address="Poltava")

contact1.save()
contact2.save()
contact3.save()
contact4.save()


contacts = Contacts.objects()

for con in contacts:
    print('Person:')
    print(f'id:{con.id}')
    print(f'First name:{con.first_name}')
    print(f'Last name:{con.last_name}')
    print(f'Birthday:{con.birthday}')
    print(f'Email:{con.email}')
    print(f'Address:{con.address}')
    for rec in con.phone:
        print(f'Phone:{rec.value}')
    print("********************")
        