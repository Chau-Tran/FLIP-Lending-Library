from util import get_book_id
import csv

class Library(object): #Chau

    def __init__(self, book_id, title, author):

        self.book_id = get_book_id(book_id)
        self.title = title
        self.author = author
        self.copies = 0
        self.times_borrowed = 0

    def just_id(self):
        return self.book_id

    def printer(self):

        print(f"\n{self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies: {self.copies}")
        print(f"Times Borrowed: {self.times_borrowed}\n")

    def dictionary(self):

        book_dictionary = {
            'id': self.book_id,
            'title': self.title,
            'author': self.author,
            'copies': self.copies,
            'times_borrowed': self.times_borrowed
        }

        return book_dictionary

    def modify(self, book_dictionary):

        self.book_id = book_dictionary['id']
        self.title = book_dictionary['title']
        self.author = book_dictionary['author']
        self.copies = book_dictionary['copies']
        self.times_borrowed = book_dictionary['times_borrowed']

    def convert_list_to_dictionary(self, list_of_books):
        
        return [x.dictionary() for x in list_of_books]

    def convert_list_to_file(self, dictionary_of_books):

        fd = open('books.csv', 'w')
        writer = csv.DictWriter(fd, fieldnames = list(dictionary_of_books[0].keys()))
        writer.writeheader()
        writer.writerows(dictionary_of_books)

        fd.close()

    def new_books(self, book_array, book_name, author_name):

        fd = open("books.csv", 'a')
        writer = csv.DictWriter(fd, fieldnames = ['id', 'title', 'author', 'copies', 'times_borrowed'])

        temp_dict = {}

        array = len(book_array)
        temp_dict["id"] = get_book_id(array)
        temp_dict["title"] = book_name
        temp_dict["author"] = author_name
        temp_dict["copies"] = 0
        temp_dict["times_borrowed"] = 0
        
        writer.writerow(temp_dict)



    def remove_book(self, book_name):

        temp_list = list()

        fd = open('books.csv', 'r')
        reader = csv.DictReader(fd)

        for book in reader:
            if book_name != book['title']:
                temp_list.append(book)

        fd_ = open('books.csv', 'w')
        writer = csv.DictWriter(fd_, fieldnames=['id','title','author','copies','times_borrowed'])
        writer.writeheader()
        writer.writerows(temp_list)


    def modify_copies_count(self, book_array, book_name, new_count):

        temp_list = list()

        fd = open('books.csv', 'r')
        reader = csv.DictReader(fd)

        for book in reader:
            if book_name != book['title']:
                temp_list.append(book)
            else:
                book['copies'] = new_count
                temp_list.append(book)

        fd_ = open('books.csv', 'w')
        writer = csv.DictWriter(fd_, fieldnames=['id','title','author','copies','times_borrowed'])
        writer.writeheader()
        writer.writerows(temp_list)

    def search_book(self, title):
        fd_book = open('books.csv', 'r')
        book_reader = list(csv.DictReader(fd_book))

        for book in book_reader:
            if book['title'] == title:
                print(f"\n{book['title']}\n{book['id']}\n{book['title']}\n{book['author']}\n{book['times_borrowed']}")

        fd_book.close()

    def search_author(self, author):

        fd_book = open('books.csv', 'r')
        book_reader = list(csv.DictReader(fd_book))

        author_list = []

        for book in book_reader:
            if book['author'] == author:
                author_list.append(book)

        print(author_list)

        fd_book.close()



def read_file():

    try: 
        fd = open('books.csv', 'r')
    except Exception as e:
        return []
    
    reader = csv.DictReader(fd)

    book_list = []
    for row in reader:
        temp_book = Library(-1, "Test", "Me")
        temp_book.modify(row)
        book_list.append(temp_book)
        
    return book_list

##################################################################################################


if __name__ == "__main__":

    book_object_0 = Library(0, "Cat in the Hat", "Dr.Seuss")
    book_object_1 = Library(1, "Rich Dad Poor Dad", "Robert T. Kiyosaki")
    book_object_2 = Library(2, "Harry Potter", "JK Rowling")
    list_of_book_objects = [book_object_0, book_object_1, book_object_2]

    book_object_dict = book_object_0.convert_list_to_dictionary(list_of_book_objects)

    book_object_0.convert_list_to_file(book_object_dict)

    

