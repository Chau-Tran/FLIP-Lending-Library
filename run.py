from book import Library, read_file
from lender import Lender, read_lenders, check_out, return_book, search_lender
import csv

def run():

    while True:
        #Chau
        book_array = read_file()

        lender_array = read_lenders()

        print("\nDASHBOARD\n\n1. Catalog \n2. Check-Out Book \n3. Return Book \n4. Lender Info \n5. Exit\n")
        choice = int(input("Enter choice: "))
        print("\n-------------------------------------------")

        if choice == 1:
            print("\nCATALOG\n\n1. View Book Collection \n2. Add Book \n3. Delete Book \n4. Modify Book Count \n5. Search for Book \n6. Search for Author\n")
            subchoice = int(input("Enter choice: "))

            if subchoice == 1:
                print("-------------------------------------------")
                for book in book_array:
                    book.printer()
                print("-------------------------------------------")


            if subchoice == 2:
                print("\nAdd New Book")

                name = input("Enter new books's title: ")
                author = input("Enter new book's author: ")
                
                book.new_books(book_array, name, author)


            if subchoice == 3:
                print("\nDelete Existing Book")

                name = input("Enter book's title: ")

                book.remove_book(name)


            if subchoice == 4:
                print("\nModify Book Count")

                name = input("Enter book title: ")
                count = int(input("Enter number of copies: "))

                book.modify_copies_count(book_array, name, count)

            if subchoice == 5:
                print("\nSearch by Book Title")

                title = input("Enter book's title: ")

                book.search_book(title)

            if subchoice == 6:
                print("\nSearch by Author")

                author = input("Enter author's name: ")

                book.search_author(author)
        
        if choice == 2:#Chau

            print("Check Out a Book")

            title = input("Enter book's title: ")
            name = input("Enter your name: ")

            check_out(title, name)

            print(f"{title} has now been checked out under you, {name}. The due date is in 7 days. Every day it is late, you will be charged $1!")

        if choice == 3:#Chau
            
            print("Check Out a Book")

            title = input("Enter book's title: ")
            name = input("Enter your name: ")

            return_book(title, name)

            print(f"{title} has now been returned. Check Lender Info tab for any penalties that may have been incurred!")

        if choice == 4: #Selma
            print("\nLENDER DASHBOARD\n\n1. View All Lenders \n2. Add Lender \n3. Remove Lender \n4. Pay Penalty \n5. Search Lender\n")
            subchoice = int(input("Enter choice: "))

            if subchoice == 1:
                print("-------------------------------------------")
                for lender in lender_array:
                    lender.print_lender()
                print("-------------------------------------------")

            if subchoice == 2:
                print("\nAdd New Lender")

                name = input("Enter new lender's name: ")
                
                lender.add_lender(lender_array, name)


            if subchoice == 3:
                print("\nRemove Existing Lender")

                name = input("Enter lender's name: ")

                lender.remove_lender(name)
            
            if subchoice == 4:

                name = input("Enter lender's name: ")

                lender.pay_penalty(name)

            if subchoice == 5:
                
                name = input("Enter lender's name: ")

                search_lender(name)

        if choice == 5:
            print("\nExiting application. Bye!\n")
            exit()



if __name__ == "__main__":
    run()