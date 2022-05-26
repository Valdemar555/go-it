import pickle
import re
import os
from collections import UserDict
from datetime import datetime, date
from copy import copy
from abc import ABC, abstractmethod

class Field:
    
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    def __str__(self) -> str:
        return self._value


class Name(Field):
    """Name class field of class Record"""
    def __init__(self,value):
        self.value = value
        if not value.isalpha():  
            raise TypeError("Please enter only letters")  

class Phone(Field):
    """Phone field of class Record"""
    @Field.value.setter
    def value(self, value):
        
        matched_phone = re.findall(r'^\+?\d+$',value)
        
        if (matched_phone and len(value) <= 15) or value == '':
            self._value = value           
        elif not matched_phone:
            print("Phone has to be no more then 15 digits and include or not '+' in the beginning")
            self._value = 'nothing'

    def __repr__(self) -> str:
        return self._value

    def __str__(self) -> str:
        return self._value  
        
    
            
class Birthday(Field):
    """Birthday field of class Record"""
    
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

class Email(Field):
    """Email field of class Record"""
    def __init__(self, value):
        if value is not None:
            if (
                re.match(r"^.+@(\w+\.){0,2}[a-z]{2,6}$", value, re.IGNORECASE)
                is not None
            ):
                super().__init__(value)
            else:
                print(f'Wrong email "{value}"!')
                self.value = None
        else:
            self.value = None


class Address(Field):
    """Adress class field of class Record"""
    def __init__(self, value):
        if value is not None:
            if value is not None and len(value) > 3:
                super().__init__(value)
            else:
                print(f'Wrong address "{value}" must be more than 3 letters')
                self.value = None
        else:
            self.value = None


class Record:
    
    def __init__(self, name, phones:list[Phone]=[], address = None, email=None, birthday=None):
        
        self.name = name
        self.phones = phones
        self.address = address
        self.email = email
        self.birthday = birthday
        self.start = 0  
               

    def add_phone(self, phone_number: str) -> None:
        phone = Phone(phone_number)
        if phone not in self.phones:
            self.phones.append(phone)

    
    def delete_phone(self, phone_arg: Phone):
        
        for item in self.phones:
            if phone_arg == item._value:
                a = self.phones.remove(item)                
                return self.phones
        print(f'Not phone number {phone_arg}')

    def _find_phone_single_value(self, phone: str):
        for ph in self.phones:
            if ph._value == phone:
                return ph

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        new_phone = Phone(new_phone)
        phone_to_remove = self._find_phone_single_value(old_phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
            self.phones.append(new_phone)
        else:    
            print("This phone not in base")


    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start > len(self.phones):
            raise StopIteration

    def __repr__(self) -> str:
        #return f"{self.phones} and {self.birhday}"
        name = self.name
        email = '---' if self.email == None else self.email
        address = '---' if self.address == None else self.address
        birthday = '---' if self.birthday == None else self.birthday
        phones = '---' if self.phones == None else self.phones
        
        return f'Phones:{self.phones}'
        
    def __str__(self):
        return f'Phones:{self.phones}'

    def __gt__(self, other):
        return self.birthday > other.birthday

    def days_to_birthday(self):
        if self.birthday:
            self.birthday = str(self.birthday)
            if len(str(self.birthday)) == 5:
                user_date = datetime.strptime(self.birthday, "%d/%m")
                current_date = datetime.now()
                user_date = user_date.replace(year=current_date.year)
                if current_date > user_date:
                    user_date = user_date.replace(year=current_date.year + 1)
                delta = user_date - current_date
                print(f"{delta.days} days left")
            else:
                user_date = datetime.strptime(self.birthday, "%d/%m/%Y")
                current_date = datetime.now()
                user_date = user_date.replace(year=current_date.year)
                if current_date > user_date:
                    user_date = user_date.replace(year=current_date.year + 1)
                delta = user_date - current_date
                print(f"{delta.days} days left")
        
    
    def get_phones(self):
        return [phone.value for phone in self.phones]

    def add_birthday(self, birthday_date):
        """
        Add 'Birthday' object
        """
        self.birthday = Birthday(birthday_date)

    def add_email(self, email):
        self.email = Email(email)

    def add_address(self, address):
        self.address = Address(address)

    def days_to_birthday(self) -> int:
        """
        If b-day is added: counts days before next one.
        """

        if self.birthday.value is None:
            print(f"No b-day added for {self.name.value}")
            return

        date_now = date.today()
        birthday_date = self.birthday.value
        birthday_date = birthday_date.replace(year=date_now.year)
        # Check if user's birthday passed this year => year + 1
        if birthday_date <= date_now:
            birthday_date = birthday_date.replace(year=date_now.year + 1)

        days_delta = birthday_date - date_now
        return days_delta.days

    def __next__(self):
        return self



class AddressBook(UserDict):
    """All contacts data"""

    printed_records = 0
    records_to_print = 0
    
    def save_data(self) -> None:
        file_name = 'contacts.bin'

        with open(file_name, "wb") as file:
            pickle.dump(self.data, file)

    def load_data(self) -> None:
        file_name = 'contacts.bin'
        with open (file_name, "rb") as file:
            self.data = pickle.load(file)
       
    
    def add_record(self, obj):

        if isinstance(obj, Record):
            self.data[obj.name.value] = obj
            return True
        
    def delete_record(self,obj):
        if isinstance(obj, Record):
            del self.data[obj.name.value]
            
            return self.data

    def __iter__(self):
         return self

    def iterator_2(self, quantity):
        self.rows_to_print = quantity

        for record in self:
            print(record)
            return record   
        
    def iterator(self, rows_number=2):
        end = len(self.data)
        i = 0
        limit = rows_number
        while True:
            yield "\n".join([f"{str(item)}" for key,item in list(self.data.items())[i:limit]])
            print("next page")
            i, limit = i + rows_number, limit + rows_number
            if i >= end:
                break  

    def __next__(self):

        if len(self.data.items()) > self.printed_records:
            
            printed_chunk = list(self.data.items())[self.printed_records:self.printed_records + self.rows_to_print]
            printed_chunk_str  = "\n".join([str(value) for key,value in printed_chunk])
            self.printed_records = self.printed_records + self.rows_to_print

            return printed_chunk_str
        else:
            print("No more records to show")
            raise StopIteration
        
    

    def __getstate__(self):
        attributes = self.__dict__.copy()
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value


    def search(self, text):
        for field in self.data.values():
            if text in field.name.value or [ph for ph in field.phones if text in ph._value]:
                print(f'{field}----serch result from----{text}')
        print('-----End of search------')        
        
            

    



def show_contacts():
    print(adress_book)

def add_contact():
    operative_name = input('Enter name of contact:\n')
    
    while operative_name == '' or operative_name in adress_book.data.keys():
        print('Hey, this name exists or it\'s not good enough\n')
        operative_name = input('Enter name of contact:\n')
    rec = Record(Name(operative_name))   
    adress_book.add_record(rec)
    
    print('Now add phone number...')
    operative_phone = input()
    ph = Phone(operative_phone)       
    while ph._value == "nothing":
        print('Add one phone number its obligatory...')
        operative_phone = input()
        ph = Phone(operative_phone)
        if operative_phone == '':
            print('Okok, fellow, let it be only the the name for now...\n\n')
            break
    rec.add_phone(operative_phone)
    adress_book.save_data()
    print('Basic contact record created\nTo add or change stuff start from MENU all over again...\nYes i like to torture HAHAHA...;)')
    return True
    #adress_book.save_data()

def del_contact(arg):
    if arg in adress_book.data.keys():
        del adress_book.data[arg]
        print('Done!!! Out of the contact book!!!!...\n')
        adress_book.save_data()
    else:
        print('You did not tell me to remember this record before ...\nIknow U know what to do for adding;)\n')
        return False
        
def find_contact(arg):
    adress_book.search(arg)
    return True

adress_book = AddressBook()
adress_book.save_data()
adress_book.load_data()

   
class ABC_Contacts(ABC):
    
    @abstractmethod
    def show_contacts(self):
        pass
    
class ABC_Commands(ABC):
    @abstractmethod
    def printCommands(self):
        pass

class All_Commands(ABC_Commands, AddressBook):   
    def printCommands(self, helper, *commands):#for example: printCommands("Fellow", contacts_commands_list, notes_command_list)
        for com in commands:
            print(f'Hello my name is {helper}.\nI can run these commands:\n  {"  ".join(com)}')
    

class Contacts(ABC_Contacts, AddressBook):
    
    def show_contacts(self):
        for record in self:
            print(record)

    
        

        
#a = Phone("+380990002233")
#print(a._value)
#b = Address("Gernigiv")
#print(b.value)
#c = Birthday("12/07")
#print(c._value)
#e = Email("dfres@ukr.net")
#print(e.value)
#d = Record(Name("Oleg"), [Phone("+380987775544"), Phone("+380978886644")])
#d=Record(Name("Dima"))
#d = Record(Name("Oleg"), [Phone("+380987775544"), Phone("+380978886644")])
#print(d.name.value)
#print(d.phones)
#print(d.birthday)
#user = AddressBook()
#d.add_phone("+380974466633")
#print(d.phones)
#d._find_phone_single_value("+380974466633")
#d.delete_phone("+380974466633")
#print(d.phones)
#d.change_phone("+380974466633", "+380990005500")
#print(d.phones)
