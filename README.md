## ECOR 1042 Group Project: Book Processor Project Version 1.0 12/04/2022

The project can be reached at:
Email: aliabdollahian@cmail.carleton.ca

### Description:
### -----------------

- The project contains a single program that allows a user to load a **csv** file containing book data. The user can then edit and organize this dataset by using the **function commands** which are:
_L: load data, A: add a book, R: remove a book, G: get books (sub-commands for G: T: by title, R: by rating, A: by author, P: by publisher, C: by category), GCT: get all categories for book title, S: sort books (sub-commands for S: T: by title, R: by rating, P: by publisher, A: by author) and Q: quit._

- The project is made of 6 files:
**T135_P2_add_remove_search_dataset.py**	A python file containing the functions to add books, remove books, and search books based on certain criteria; those being: title, rating, author, publisher, category and get all categories by book title.
    
    **T135_P3_sorting_fun.py**			A python file containing functions that allow the user to sort books based on different criteria; those being: title, rating, publisher and author.
    
    **T135_check_equal.py**			A python file that checks if the functions T135\_P2\_add\_remove\_search\_dataset.py and T135\_P3\_sorting\_fun.py produce the expected outcomes.
    
    **T135_P4_booksUI.py**				A python file that contains the function for the user interface of the program. This file calls on the other 3 functions to execute the user's commands.
    
    **T135_P5_load_data.py**			A python file that takes in a csv file of book information and converts it into the format required to work with the program.

    **README .md**                      This markdown file which contains information on how to install and use this program as well as contact information, creadit, version number, date published, project description, etc.

### Installation:
### -----------------

**Python 3.10.4 or later must be installed.**
Only built-in python modules are used. No external modules must be loaded.

### Usage:
### ----------
**In the command line once you have arrived in the correct directory, type:**
>python T135_P4_booksUI.py

- This software is a text-based interactive user interface that allows the user to load a **csv** file containing book information. The user can then use the software command to manipulate the book data. 
- **The availible commands are:** _L: load data, A: add a book, R: remove a book, G: get books (sub-commands for G: T: by title, R: by rating, A: by author, P: by publisher, C: by category), GCT: get all categories for book title, S: sort books (sub-commands for S: T: by title, R: by rating, P: by publisher, A: by author) and Q: quit._ 

- When using this program, the first command the user should use is L to load a csv file containing book information in a table with columns named (title, author, rating, publisher, pages, category, language), each book should take up a row with its information in the afformentioned order. If the user does not use L as the first command, the program will display the message "file not loaded" followed by the menu of commands. 
- After loading an appropriate file, the user can choose a command from the menu and follow the program's instructions at each step. If the user attempts to use aninvalid command, the program will display the message "no such command" followed by the menu of commands. 
- The Q command (quit) terminates the program. All commands can be typed in either lower or upper case.

### Credits:
### -----------

**Ali Abdollahian** - _Author of Functions:_ book_category_dictionary, get_books_by_category, get_books_by_rate, test_get_books_by_title, test_get_books_by_author, sort_books_title,
test_sort_books_ascending_rate, T135_P4_UI_case2.

**Daniele Caruso** - _Author of Functions:_ add_book, remove_book, test_get_books_by_publisher, test_get_all_categories_for_book_title, sort_books_author, test_sort_books_publisher,
T135_P4_UI_case1.

**Keegan Kilfoil** - _Author of Functions:_ book_category_dictionary, get_books_by_publisher, get_all_categories_for_book_title, test_add_book, test_remove_book, sort_books_publisher,
test_sort_books_author, T135_P4_UI_case4.

**Yancheng Ding** - _Author of Functions:_ get_books_by_title, get_books_by_author, test_get_books_by_category, test_get_books_by_rate, sort_books_ascending_rate, test_sort_books_title,
T135_P4_UI_case3.

Copyright 2022 Ali Abdollahian, Daniele Caruso, Keegan Kilfoil and Yancheng Ding
