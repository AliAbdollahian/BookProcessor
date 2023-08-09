#ECOR 1042 T135 Group Project Milestone 2 Task 2 P4 User Interface Team Code
#Ali Abdollahian 101229396
#Daniele Caruso 101220647
#Yancheng Ding 101223452
#Keegan Kilfoil 101220476
#2022-04-11
#Version 1.0

import string
from typing import List
from T135_P2_add_remove_search_dataset import add_book, remove_book, get_books_by_category, get_books_by_rate, get_books_by_title, get_books_by_author, get_books_by_publisher, get_all_categories_for_book_title
from T135_P5_load_data import book_category_dictionary
from T135_P3_sorting_fun import sort_books_title, sort_books_author, dictionary_to_list, sort_books_publisher, sort_books_ascending_rate

def create_interface():
    """
    Creates a user interface to provide the user with commands.
    
    create_interface() prints:
     1- L)oad Data
     2- A)dd book
     3- R)emove book
     4- G)et books
	T)itle	R)ate	A)uthor	P)ublisher	C)ategory
     5- GCT) Get all Categories for book Title
     6- S)ort books
	T)itle	R)ate	P)ublisher	A)uthor
     7- Q)uit
    """
    print("The available commands are:\n 1- L)oad Data\n 2- A)dd book\n 3- R)emove book\n 4- G)et books\n\tT)itle\tR)ate\tA)uthor\tP)ublisher\tC)ategory\n 5- GCT) Get all Categories for book Title\n 6- S)ort books\n\tT)itle\tR)ate\tP)ublisher\tA)uthor\n 7- Q)uit")

def get_command():
    """
    Precondition: No Precondition

    Creates a user interface that allows the user to load a csv data file and add books to it, remove books from it, get books by: title, rate, author, publisher and category, get all categories for a certain book title, and sort books by: title, rate, publisher and author. To quit the function the user must type Q or q. The interface provides instructions for how to procede when each a command is used.
    """
    list_of_supported_commands=["G","R","A","T","L","GCT","P","C","S","Q"]
    command=""
    all_books = ""

    while command.upper() != "Q" :
        create_interface()
        command=input("Please type your command: ")
        
        if command.upper() not in list_of_supported_commands:
            print("No such command")
            
        else:
            
            if command.upper()=="L":
                try:
                    all_books = book_category_dictionary(input("Please enter the name of the file to be loaded: "))
                    print(all_books)
                    print("File Loaded Succesfully")
                except FileNotFoundError:
                    print("Failed to load file: File does not exist")
                    
            elif command.upper() == "G" and type(all_books) == dict:
                specific = input ("How do you want to get a book? ")
                specific_upper = specific.upper()
                if specific_upper == "R":
                    get_rate=int(input("Please type the rate you are looking for? "))
                    print(get_books_by_rate(all_books,get_rate))
                elif specific_upper == "A":
                    get_author=input("Please type name of author whom you are looking for? ")
                    print(get_books_by_author(all_books,get_author))
                elif specific_upper == "T":
                    get_title=input("Please type title you are looking for? ")
                    print(get_books_by_title(all_books,get_title))
                elif specific_upper=='P':
                    name=input('publisher name:')
                    print(get_books_by_publisher(all_books,name))
                elif specific_upper=='C':
                    name=input('category name:')
                    print(get_books_by_category(all_books,name))                
                    
            elif command.upper() == "A" and type(all_books) == dict:
                book = (input("Please enter the book information in the following form: title,author,rating,publisher,pages,category,language (no parentheses, spaces or quotation marks): "))
                book = book.split(",")
                book = tuple(book)
                print(book)
                add_dict = add_book(all_books, book)
                 
            elif command.upper() == "R" and type(all_books) == dict:            
                title = input("Please enter the title of the book you wish to remove (no quotation marks): ")
                category = input("Please enter the book's category (no quotation marks): ")
                remove_dict = remove_book(all_books, title, category)           
            
            elif command.upper()=='GCT' and type(all_books) == dict:
                name=input('Book title:')
                print(get_all_categories_for_book_title(all_books,name))
                
            elif command.upper() == "S" and type(all_books) == dict:
                if type(all_books) == dict:
                    loaded_list = dictionary_to_list(all_books)
                    sorting_method = input("How do you want to sort? ")
                    sorting_method = sorting_method.upper()
                    if sorting_method == "T":
                        sorted_list = sort_books_title(all_books)
                        print(sorted_list)
                    elif sorting_method == "R":
                        sorted_list = sort_books_ascending_rate(all_books)
                        print(sorted_list)
                    elif sorting_method == "P":
                        sorted_list = sort_books_publisher(all_books)
                        print(sorted_list)  
                    elif sorting_method == "A":
                        sorted_list = sort_books_author(all_books)
                        print(sorted_list)            
                
            elif command.upper()!="Q":
                print("File not loaded")

# Main script 
if __name__ == "__main__":
    get_command()