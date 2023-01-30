from Address_book.AdressBook import address_Book
#from Sorter.sort import start_sorting
from Notebook.notes import notepad


def main(u_input):

    if u_input == "1":
        print("Address book")
        # address_Book()

    if u_input == "2":
            print("Sort")
            start_sorting()

    if u_input == "3":
            print("Notepad")
            notepad()


if __name__ == "__main__":
    while True:
        u_input = input(
            "Choose what you want to use: \n1) Address book \n2) sorter \n3) Notepad \n>>>").lower()
        main(u_input)

        if u_input in [".", "exit"]:
            print("Good bye!")
            break