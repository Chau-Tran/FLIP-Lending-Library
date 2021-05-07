import random 
import csv 
from datetime import date
from util import get_user_id
from book import Library

class Lender(object): #Selma

    def __init__(self, unique_id, name, book):

        self.unique_id = unique_id
        self.name = name
        self.book = book
        self.date_borrowed = None
        self.penalty_owed = 0

    def print_lender(self):

        print(f"Unique ID: {self.unique_id}")
        print(f"Name: {self.name}")
        print(f"Book: {self.book}")
        print(f"Date: {self.date_borrowed}")
        print(f"Penalty: {self.penalty_owed}")
        print("============")

    def modify(self, lender_dictionary):

        self.unique_id = lender_dictionary['unique_id']
        self.name = lender_dictionary['name']
        self.book = lender_dictionary['book']
        self.date_borrowed = lender_dictionary['date_borrowed']
        self.penalty_owed = lender_dictionary['penalty_owed']


    def add_lender(self, lender_array, lender):
        csv_fd = open("lenders.csv", 'a')
        csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
        
        lender_dict = {}
        
        array = len(lender_array)
        lender_dict["name"] = lender
        lender_dict["unique_id"] = get_user_id(array)
        lender_dict["book"] = None
        lender_dict["date_borrowed"] = None
        lender_dict["penalty_owed"] = 0
        
        csv_writer.writerow(lender_dict)

    def remove_lender(self, lender):

        lines = list() 
        with open('lenders.csv', 'r') as read_file:
            reader = csv.DictReader(read_file)

            for row in reader:
                if row['name'] != lender:
                    lines.append(row) 
                    
        with open('lenders.csv', 'w') as write_file:
            writer = csv.DictWriter(write_file, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
            writer.writeheader()
            writer.writerows(lines)

    def pay_penalty(self, lender):

        fd_lender = open('lenders.csv', 'r')
        lender_list = list(csv.DictReader(fd_lender))

        for lender in lender_list:
            if lender['name'] == lender:

                fines = lender['penalty_owed']
                print(f"You owe ${fines}.")

                paid = input("How much will you like to pay off? ")
                new_balance = fines - paid

                lender['penalty_owed'] = new_balance

                print(f"Your new balance is {new_balance}")

        fd_lender.close()

        fd_lender = open('lenders.csv', 'w')
        writer = csv.DictWriter(fd_lender, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
        writer.writeheader()
        writer.writerows(lender_list)

def search_lender(lender):

    fd_lender = open('lenders.csv', 'r')
    lender_reader = list(csv.DictReader(fd_lender))

    for lender in lender_reader:
        if lender['name'] == lender:
            
            id_ = lender['unique_id']
            name = lender['name']
            book = lender['book']
            date =lender['date_borrowed']
            penalty =lender['penalty_owed']
            
            print(f"\n{id_}")
            print(f"Name: {name}")
            print(f"Book: {book}")
            print(f"Date Borrowed: {date}")
            print(f"Penalties: {penalty}\n")


def check_out(title, name):

    fd_book = open('books.csv', 'r')
    book_reader = list(csv.DictReader(fd_book))

    fd_lender = open('lenders.csv', 'r')
    lender_reader = list(csv.DictReader(fd_lender))

    for book in book_reader:
        if book['title'] == title:
            if int(book['copies']) > 0:
                for lender in lender_reader:
                    if lender['name'] == name:
                        if int(lender['penalty_owed']) <= 10:

                            lender['book'] = title
                            lender['date_borrowed'] = date.today()
                            book['copies'] = (int)(book['copies']) - 1
                            book['times_borrowed'] = (int)(book['times_borrowed']) + 1
                    
                        else:
                            print("You have a withstanding balance of $10 or more, please settle this penalty before you check out another book :(")
            else:
                print("No more copies are available :( ")

    fd_book = open('books.csv', 'w')
    writer = csv.DictWriter(fd_book, fieldnames = ['id', 'title', 'author', 'copies', 'times_borrowed'])
    writer.writeheader()
    writer.writerows(book_reader)

    fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(fd_lender, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
    writer.writeheader()
    writer.writerows(lender_reader)

    fd_book.close()
    fd_lender.close()

def return_book(title, name):

    fd_book = open('books.csv', 'r')
    book_reader = list(csv.DictReader(fd_book))

    fd_lender = open('lenders.csv', 'r')
    lender_reader = list(csv.DictReader(fd_lender))

    for lender in lender_reader:
        if lender['name'] == name:
            if lender['book'] == title:
                book_title = lender['book']
                if book_title != '':
                    borrowed_date_list = lender['date_borrowed'].split('-')
                    borrowed_date = date(int(borrowed_date_list[0]), int(borrowed_date_list[1]), int(borrowed_date_list[2]))

                    for book in book_reader:
                        if book['title'] == title:
                            book['copies'] = (int)(book['copies']) + 1
                            today = date.today()
                            days_passed = (today - borrowed_date).days
                            if days_passed > 7:
                                lender['penalty'] = (int)(lender['penalty']) + (days_passed - 7)

                    lender['book'] = None
                    lender['date_borrowed'] = None

    fd_book = open('books.csv', 'w')
    writer = csv.DictWriter(fd_book, fieldnames = ['id', 'title', 'author', 'copies', 'times_borrowed'])
    writer.writeheader()
    writer.writerows(book_reader)

    fd_lender = open('lenders.csv', 'w')
    writer = csv.DictWriter(fd_lender, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
    writer.writeheader()
    writer.writerows(lender_reader)    

    fd_book.close()
    fd_lender.close()   



def read_lenders():

    try: 
        fd = open('lenders.csv', 'r')
    except Exception as e:
        return []
    
    reader = csv.DictReader(fd)

    lender_list = []
    for row in reader:
        temp_lender = Lender(-1, "Test", "Me")
        temp_lender.modify(row)
        lender_list.append(temp_lender)
        
    return lender_list

def write_file():
    lender_list = []
    lender_listofdicts = []
    name_list = ['Ross', 'Chandler', 'Joey', 'Rachel', 'Monica', 'Phoebe', 'Harry', 'Louis', 'Liam', 'Niall']
    
    csv_fd = open("lenders.csv", 'w')
    
    csv_writer = csv.DictWriter(csv_fd, fieldnames = ['unique_id', 'name', 'book', 'date_borrowed', 'penalty_owed'])
    csv_writer.writeheader()

    for i in range(10):
        lender_dict = {} 
        name = name_list[i]
        unique_id = f"Lender_{i + 1}"
        book = None
        date_borrowed = None
        penalty_owed = 0
        
        lender_dict["name"] = name
        lender_dict["unique_id"] = unique_id
        lender_dict["book"] = book
        lender_dict["date_borrowed"] = date_borrowed
        lender_dict["penalty_owed"] = penalty_owed

        lender_listofdicts.append(lender_dict)

        lender_1 = Lender(unique_id, name, book) 
        
        lender_list.append(lender_1)

    csv_writer.writerows(lender_listofdicts)

    return lender_list


if __name__ == "__main__":
    write_file()






