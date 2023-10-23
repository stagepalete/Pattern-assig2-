class LibraryItem:
    def checkout(self):
        pass

    def return_item(self):
        pass

class PrintedBook:
    def check_out(self):
        print("Checked out the printed book")

    def return_it(self):
        print("Returned the printed book")

class EBook:
    def borrow(self):
        print("Borrowed the e-book")

    def send_back(self):
        print("Sent back the e-book")

class PrintedBookAdapter(LibraryItem):
    def __init__(self, printed_book):
        self.printed_book = printed_book

    def checkout(self):
        self.printed_book.check_out()

    def return_item(self):
        self.printed_book.return_it()


class EBookAdapter(LibraryItem):
    def __init__(self, ebook):
        self.ebook = ebook

    def checkout(self):
        self.ebook.borrow()

    def return_item(self):
        self.ebook.send_back()

def process_item(item):
    item.checkout()
    item.return_item()




def main():
    printed_book = PrintedBook()
    ebook = EBook()

    printed_book_adapter = PrintedBookAdapter(printed_book)
    ebook_adapter = EBookAdapter(ebook)

    print("Using the Adapter for Printed Book:")
    process_item(printed_book_adapter)

    print("\nUsing the Adapter for E-Book:")
    process_item(ebook_adapter)

if __name__ == '__main__':
    main()