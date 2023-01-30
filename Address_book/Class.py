from collections import UserDict
from datetime import datetime
from itertools import islice


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value}"

    def __repr__(self):
        return f"{self.value}"


class Birthday(Field):
    # (рік-місяць-день)
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val: str):
        data = val.split("-")
        if not "".join(data).isdigit():
            raise ValueError
        if int(data[0]) > datetime.now().year or int(data[1]) > 12 or int(data[2]) > 30:
            raise ValueError
        self.__value = val


class Name(Field):
    def __init__(self, value):
        self.value = value.capitalize()


class Phone(Field):

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val: str):
        if not len(val) == 10 and not len(val) == 13 and not val.lstrip("+").isdigit():
            raise ValueError
        if len(val) == 10:
            val = "+38" + val
        if not val[3] == "0":
            raise ValueError
        self.__value = val


class Record():
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.name = name
        self.phones = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)

    def __str__(self):
        return f"{self.name} - {', '.join([str(p) for p in self.phones])}"

    def __repr__(self):
        return f"{self.name} - {', '.join([str(p) for p in self.phones])}"

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def delete_phone(self, phone: Phone):
        for p in self.phones:
            if p.value == phone.value:
                self.phones.remove(p)
                return f'Phone {p.value} delete successful.'
        return f'Phone {phone.value} not found'

    def get_days_from_today(self):
        # (рік-місяць-день)
        if not self.birthday.value:
            print("Birthday not entered")
        else:
            date1 = self.birthday.value.split("-")
            date = datetime(year=datetime.now().year, month=int(
                date1[1]), day=int(date1[2]))
            data_now = datetime.now()
            dat = date - data_now
            return dat.days


class AddressBook(UserDict):
    index = 0

    def add_record(self, rec: Record):
        self[rec.name.value] = rec

    def __str__(self):
        return '\n'.join([str(i) for i in self.values()])

    def iteration(self, step=5):
        while AddressBook.index < len(self):
            yield list(islice(self.items(), AddressBook.index, AddressBook.index+step))
            if AddressBook.index > len(self):
                raise StopIteration()
            AddressBook.index += step
