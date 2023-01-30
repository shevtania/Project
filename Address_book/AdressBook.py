from collections import UserDict
from Address_book.Class import *
from datetime import datetime
import pickle
try:
    with open("Address_book/AddressBook.txt", "rb") as file:
        ab = pickle.load(file)
except:
    ab = AddressBook()
pages = []


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return "Sorry, try again"
        except ValueError:
            print("incorrect input")
        except KeyError:
            print("incorrect Name")
    return wrapper


def greetings(*args):
    print("How can I help you?")


@input_error
def add(*argv):
    phone, birthday = None, None
    name = Name(argv[0][0])
    if len(argv[0]) >= 2:
        phone = Phone(argv[0][1])
    if len(argv[0]) >= 3:
        birthday = Birthday(argv[0][2])
    ab.add_record(Record(name, phone, birthday))


@input_error
def add_phon(*argv):
    ab[argv[0][0]].add_phone(Phone(argv[0][1]))


@input_error
def change(*argv):
    if len(argv[0]) == 3:
        ab[argv[0][0].title()].add_phone(Phone(argv[0][2]))
        ab[argv[0][0].title()].delete_phone(Phone(argv[0][1]))
    else:
        print("To change the number, enter the name of the contact, the number to change, the new phone number")


@input_error
def del_phone(*argv):
    ab[argv[0][0].title()].delete_phone(Phone(argv[0][1]))


@input_error
def show_all(*argv):
    print(ab)


@input_error
def page(*argv):
    reg = ab.iteration(2)
    for b in reg:
        pages.append(b)
    print(f"page {int(argv[0][0])} of {len(pages)}")
    for i in pages[int(argv[0][0]) - 1]:
        print(i[1])


@input_error
def output_phone(name):
    print(ab[name[0].title()])
    if ab[name[0].title()].birthday:
        print(f"Birthday: {ab[name[0].title()].birthday}")


@input_error
def add_birthday(name):
    print(ab[name[0].title()])


@input_error
def day_birthday(name):
    print(ab[name[0].title()].get_days_from_today())


@input_error
def search(val):
    if val[0].isdigit():
        for p in ab.items():
            for x in p[1].phones:
                if not str(x).find(val[0]) == -1:
                    print(p[1])
    else:
        for p in ab.items():
            if not p[0].lower().find(val[0].lower()) == -1:
                print(p[1])


COMMANDS = {
    greetings: "hello",
    add: "add",
    add_phon: 'append',
    change: "change",
    output_phone: "phone",
    show_all: "show",
    del_phone: "del",
    add_birthday: "birthday",
    day_birthday: "day",
    page: "page",
    search: "search"
}


def command_parser(u_input: str):
    for comand, key_words in COMMANDS.items():
        if u_input.startswith(key_words):
            return comand, u_input.replace(key_words, "").strip().split(" ")
    return None, None


def address_Book():
    print("Address book open")

    while True:
        u_input = input(">>>")
        u_input = u_input.lower()
        if u_input in [".", "good bye", "close", "exit", "/", ]:
            print("Good bye!")
            break
        comand, data = command_parser(u_input)
        if not comand:
            print("Enter command")
        else:
            comand(data)

    with open("Address_book/AddressBook.txt", "wb") as file:
        pickle.dump(ab, file)

    # return ab


# if __name__ == "__main__":
#     try:
#         with open("AddressBook.txt", "rb") as file:
#             ab = pickle.load(file)
#     except:
#         pass
#     main()
#     with open("AddressBook.txt", "wb") as file:
#         pickle.dump(ab, file)
