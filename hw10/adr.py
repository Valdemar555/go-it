from collections import UserDict

class Field:
    def __init__(self,value):
        self.value = value

class Name (Field):
    def __init__(self,value):
        self.value = value
        if not value.isalpha():  
            raise TypeError("Please enter only letters")  


class Phone(Field):
    def __init__(self,value):
        self.value = value
        if not value.isdigit():  
            raise TypeError("Please enter only digits")  
        if len(self.value)<10:
            raise ValueError("Please enter 10-digits phone number")

    def __repr__(self) -> str:
        return self.value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return self.value == other.value
        
   
class Record():
    def __init__(self, name: Name, phones:list[Phone]=[]):
        self.name = name
        self.phones = phones
        self.start = 0

    def add_phone(self, new_phone:Phone):
        self.phones.append(new_phone)
        print("Phone add successfully.")
        return self.phones

    def del_phone(self, new_phone:Phone):
        if new_phone in self.phones:
            self.phones.remove(new_phone)
            
        else:
            print("This phone not in base")
        return self.phones
    
        
    def change_phone(self, old_phone:Phone, new_phone:Phone):
        if old_phone in self.phones:
            for x, result in enumerate(self.phones):
                    if result == old_phone:
                        self.phones[x]=new_phone
                        print(self.phones)
        else:
            print("This phone not in base")
        return self.phones

    def __iter__(self):
        return self

    def __next__(self):
        self.start +=1
        if self.start > len(self.phones):
            raise StopIteration

    def __repr__(self) -> str:
        return self.phones

    def __str__(self) -> str:
        return self.phones

class AddressBook(UserDict):
    
    def add_record(self, other:Record):
        key = other.name.value
        value = other.phones
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data[key] = value
        print(self.data)
        
                
    def del_record(self,other):
        if other in self.data:
            self.data.pop(other)
            print(self.data)


d = Record(Name("Oleg"), [Phone("0987775544"), Phone("0978886644")])
#d=Record(Name("Dima"))
#print(d.name.value)
#print(d.phones)
user = AddressBook()
#d.add_phone(Phone("0974466633"))
#print(d.phones)
#.del_phone(Phone("0974466633"))
#print(d.phones)
#d.change_phone(Phone("0978886644"), Phone("0990005500"))
#print(d.phones)
#user.add_record(Record((Name("Vasja")), [Phone("0931212333"), Phone("0971458558")]))
#user.add_record(Record((Name("Vanja")), [Phone("0975557788")]))
#user.add_record(Record((Name("Julia")), []))
#user.del_record("Julia")
