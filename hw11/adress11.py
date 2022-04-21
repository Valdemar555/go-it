from collections import UserDict
from datetime import datetime
import itertools


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        self.value = value
        if not value.isalpha():
            raise TypeError("Please enter only letters")


class Phone(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value.isdigit() and len(new_value) == 10:
            self._value = new_value
        else:
            raise ValueError("Please enter 10-digits phone number")

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Birhday(Field):
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if len(new_value) == 5 or len(new_value) == 10:
            self._value = new_value
        else:
            raise ValueError("Please enter data in format dd/mm/yyyy or dd/mm")

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return self.value == other.value


class Record:
    def __init__(self, name: Name, phones: list[Phone] = [], birhday: Birhday = ""):
        self.name = name
        self.phones = phones
        self.birhday = birhday
        self.start = 0

    def add_phone(self, new_phone: Phone):
        self.phones.append(new_phone)
        print("Phone add successfully.")
        return self.phones

    def del_phone(self, new_phone: Phone):
        if new_phone in self.phones:
            self.phones.remove(new_phone)
        else:
            print("This phone not in base")
        return self.phones

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        if old_phone in self.phones:
            for x, result in enumerate(self.phones):
                if result == old_phone:
                    self.phones[x] = new_phone
                    # print(self.phones)
        else:
            print("This phone not in base")
        return self.phones

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > len(self.phones):
            raise StopIteration

    def __repr__(self) -> str:
        return f"{self.phones} and {self.birhday}"

    def __str__(self) -> str:
        return f"{self.phones} and {self.birhday}"

    def __gt__(self, other):
        return self.birhday > other.birhday

    def days_to_birthday(self):
        if self.birhday:
            self.birhday = str(self.birhday)
            if len(str(self.birhday)) == 5:
                user_date = datetime.strptime(self.birhday, "%d/%m")
                current_date = datetime.now()
                user_date = user_date.replace(year=current_date.year)
                if current_date > user_date:
                    user_date = user_date.replace(year=current_date.year + 1)
                delta = user_date - current_date
                print(f"{delta.days} days left")
            else:
                user_date = datetime.strptime(self.birhday, "%d/%m/%Y")
                current_date = datetime.now()
                user_date = user_date.replace(year=current_date.year)
                if current_date > user_date:
                    user_date = user_date.replace(year=current_date.year + 1)
                delta = user_date - current_date
                print(f"{delta.days} days left")

class AddressBook(UserDict):
    def add_record(self, other: Record):
        key = other.name.value
        value = other.phones
        birhday = other.birhday
        if key in self.data:
            self.data[key].append[value, birhday]
        else:
            self.data[key] = [value, birhday]
        print(self.data)

    def del_record(self, other):
        if other in self.data:
            self.data.pop(other)
            print(self.data)

    def next_page(self, rec_on_page):
        end = len(self)
        i = 0
        limit = rec_on_page
        while True:
            result = "\n".join(
                [f"{k} : {v}" for k, v in itertools.islice(self.items(), i, limit)]
            )
            yield result + "\n"
            i, limit = i + rec_on_page, limit + rec_on_page
            if i >= end:
                break
