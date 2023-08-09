#ECOR 1042 Group Project Milestone 1 Task 3 Team Code
#Ali Abdollahian 101229396
#Daniele Caruso 101220647
#Yancheng Ding 101223452
#Keegan Kilfoil 101220476
#2022-04-11
#Version 1.0

import string
from typing import List
from T135_check_equal import check_equal 

#Test Dictionaries for add_book and remove_book since testing these functions by manually adding and removing books from the full google dictionary is inefficient and prone to errors. TA David confirmed this
#Since the functions tested either add or remove a book, each test dictionary has a version with and without the book in it. Also, since the dictionaries are modified when called with these functions, temporary dictionaries have been created. This is so the call functions are clean and easy to understand

TEST_DICTIONARY_A_WITHOUT_BOOK = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Comics':[{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}]}

test_dictionary_A_without_book = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Comics':[{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}]}

TEST_DICTIONARY_A_WITH_BOOK = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Harry Poter', 'author': 'JK Rowling', 'rating': 5.0, 'publisher': 'The Publisher', 'pages': 100, 'category': 'Fiction', 'language': 'English'}], 'Comics':[{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}]}

test_dictionary_A_with_book = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Harry Poter', 'author': 'JK Rowling', 'rating': 5.0, 'publisher': 'The Publisher', 'pages': 100, 'category': 'Fiction', 'language': 'English'}], 'Comics':[{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}]}

TEST_DICTIONARY_B_WITHOUT_BOOK = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Evolution': []}

test_dictionary_B_without_book = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}]}

TEST_DICTIONARY_B_WITH_BOOK = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Evolution': [{'title': 'On the Origin of Species', 'author': 'Charles Darwin', 'rating': 4.0, 'publisher': 'Simon and Schuster', 'pages': 502, 'category': 'Evolution', 'language': 'English'}]}

test_dictionary_B_with_book = {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Evolution': [{'title': 'On the Origin of Species', 'author': 'Charles Darwin', 'rating': 4.0, 'publisher': 'Simon and Schuster', 'pages': 502, 'category': 'Evolution', 'language': 'English'}]}

TEST_DICTIONARY_C = {'category': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category', 'language': 'language'}], 'category2': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category2', 'language': 'language'}]}

test_dictionary_C_1 = {'category': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category', 'language': 'language'}], 'category2': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category2', 'language': 'language'}]}

test_dictionary_C_2 = {'category': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category', 'language': 'language'}], 'category2': [{'title': 'title', 'author': 'author', 'rating': 1, 'publisher': 'publisher', 'pages': 1, 'category': 'category2', 'language': 'language'}]} #This dictionary needs to be called for both functions so two modifiable dictionaries are required

#Functions
def book_category_dictionary(filename:str)->dict[str:str]:
 """
 Returns a dictionary with the stored data based on the category of file google_books_dataset.csv as filename 
 >>>book_category_dictionary("google_books_dataset.csv")
 {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'},...]}
 """
 all_books={}
 count=0
 infile = open(filename, "r")
 count=0
 for line in infile:
   count+=1
   if count==1:
    pass 
   else:
    category = line.split(",")
    data_dic={}
    data_dic["title"]=category[0]
    data_dic["author"]=category[1]
    if category[2] != ("N/A"): #becouse in manual noted it should be float 
     data_dic["rating"]=float(category[2])
    data_dic["publisher"]=category[3]
    data_dic["pages"]=int(category[4])
    data_dic["category"]=category[5]
    data_dic["language"]=category[6]
    if not category[5] in all_books:
          all_books[category[5]]=[] 
    all_books[category[5]]+=[data_dic]
 infile.close()
 return (all_books)


def add_book (receiving_dict: dict, book: tuple) -> dict:
    
    """
    Returns the receiving dictionary (receiving_dict) with the indicated new book (book)
    added to the value of the category key.
    
    >>> add_book (all_books, ("Harry Poter and the Philosophers Stone", "JK Rowling", 4.5, "Bloomsbury", 223, "Fiction", "English"))
    The book has been added correctly
   {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'},... {'title': 'Harry Poter and the Philosophers Stone', 'author': 'JK Rowling', 'rating': 4.5, 'publisher': 'Bloomsbury', 'pages': 223, 'category': 'Fiction', 'language': 'English'}], 'Comics':[{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}, ...
   
   >>> add_book (all_books, ("On the Origin of Species", "Charles Darwin", 4.0, "Simon and Schuster", 502, "Evolution", "English"))
   {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'},... 'Evolution': [{'title': 'On the Origin of Species', 'author': 'Charles Darwin', 'rating': 4.0, 'publisher': 'Simon and Schuster', 'pages': 502, 'category': 'Evolution', 'language': 'English'}]}
    """
    
    book_dict = {"title":book[0], "author": book[1], "rating":book[2], "publisher":book[3], "pages":book[4], "category":book[5], "language":book[6]}
    
    for category in receiving_dict:
        if category == book_dict["category"]:
            receiving_dict[category].append (book_dict)
            print ("The book has been added correctly")
            return receiving_dict
        elif book_dict["category"] not in receiving_dict.keys(): 
            receiving_dict.update ({book_dict["category"]:[book_dict]})
            print ("The book has been added correctly")
            return receiving_dict
        else:
            print ("There was an error adding the book")
            return receiving_dict

def remove_book (removing_dict: dict, title: str, category: str) -> dict:
    
    """
    Returns the dictionary (removing_dict) with the specified book (specified by its title and category)
    removed from the value of the category key.
    
    test = remove_book (all_books, "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'Fiction')
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English\n'}, ... 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Investing', 'language': 'English\n'}]} 
    """
    
    for book in removing_dict[category]:
        if book["title"] == title:
            removing_dict[category].remove(book)
            print ("The book has been removed correctly")            
            return removing_dict    
        
    else:
        print ("There was an error removing the book. Book not found.")
        return removing_dict
    

def get_books_by_category(data:dict,category:str)->int:
    """
    Return the number of books for asked category and all the books on that category asked and their titles with authors
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Horror")
    The category Horror has 1 books. This is the list of books:
    Book 1 : The Mysterious Affair at Styles by Agatha Christie
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Fiction")
    39
    >>>get_books_by_category(book_category_dictionary("google_books_dataset.csv"),"Comics")
    7
    """
    count=0
    selected=data.get(category)
    print("The category",category,"has",len(selected),"books.","This is the list of books:")
    for elem in selected:
        count+=1
        extarct_authors=elem.get("author")
        extract_titles=elem.get("title")
        print("Book",count,":",extract_titles,"by",extarct_authors)
    return count
        
        
def get_books_by_rate(data:dict,rating:int)->float:
    """
    Return the number of books for asked rating range which is all the asked rate and its decimals and all the books in the 
    asked rate range and their titles with authors
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),5)
    13
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),4)
    152
    >>>get_books_by_rate(book_category_dictionary("google_books_dataset.csv"),3)
    19
    """
    count=0
    lst=[]
    for i in data:
        selected=data.get(i) 
        for elem in selected:
                extract_rates=elem.get("rating")
                if extract_rates!= None and rating <= extract_rates < rating+1:
                        lst+=[elem]
                        count+=1
    print("There are",count,"books whose rate is between",rating,"and",rating+1,".","This is the list of books:") 
    count=0
    for k in lst:
        count+=1
        extarct_authors=k.get("author")
        extract_titles=k.get("title") 
        print("Book",count,":",extract_titles,"by",extarct_authors)
    return count


def get_books_by_title(data:dict,title:str)->bool:
    """
    Returns True if the book can be found in the dictionary, else False.
    >>>get_books_by_title(dictionary,"Antiques Con")
    True
    >>>get_books_by_title(dictionary,"Antiques A Con")
    False
    >>>get_books_by_title(dictionary,"Antiques Chop")
    True
    """
    found=False
    cata_values=data.values()
    for cata_value in cata_values:
        for lst in cata_value:
            if lst.get('title')==title:
                found=True
    if found==True:
        print("The book has been found")
    else:
        print("The book has NOT been found")
    return found

def get_books_by_author(data:dict,name:str)->int:
    """
    Returns number of books created by the author whose name is given.
    >>>get_books_by_author(dictionary,"Barbara Allan")
    4
    >>>get_books_by_author(dictionary,"Peter V. Brett")
    1
    >>>get_books_by_author(dictionary,"Brandon Sanderson")
    2
    """
    title=[]
    rating=[]
    cata_values=data.values()
    for cata_value in cata_values:
        for lst in cata_value:
            if lst.get('author')==name:
                if lst.get('title') not in title:
                    title.append(lst.get('title'))
                    rating.append(lst.get('rating'))
    print("The author "+name+" has published the following books:")
    num=0
    for books in title:
        book=title[num]
        score=rating[num]
        print("Book "+str(num+1)+": "+books+", rate: "+str(score))
        num+=1
    return len(title)

def get_books_by_publisher(dictionary:dict, publisher_name:str) -> int:
    """
    Returns the number of books in the dictionary published by a given publisher
    
    get_books_by_publisher(open('google_books_dataset.csv'), "Simon and Schuster")
    Prints: The publisher Simon and Schuster has published the following books:
            Book 1: The Memoirs of Sherlock Holmes by Arthur Conan Doyle
            Book 2: How To Win Friends and Influence People by Dale Carnegie
            Book 3: Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
            Book 4: Principles: Life and Work by Ray Dalio
    Returns: 4
    """
    books_published = set()
    print("The publisher " + publisher_name + " has published the following books:")
    for category in dictionary:
        for book in dictionary[category]:
            if book["publisher"] == publisher_name:
                books_published.add(book["title"] + " by " + book["author"])
    book_count = 1
    for book in books_published:
        print("Book " + str(book_count) + ": " + book)
        book_count += 1
    return len(books_published)
   
def get_all_categories_for_book_title(dictionary:dict, book_title:str) -> int:
    """
    Returns the number of categories in the dictionary associated with the given book title
    
    get_all_categories_for_book_title(open('google_books_dataset.csv'), "How To Win Friends and Influence People")
    Prints: The book title How To Win Friends and Influence People belongs to the following categories:
            Category 1: Psychology
            Category 2: Economics
    Returns: 2
    """
    book_categories = set()
    print("The book title " + book_title + " belongs to the following categories:")
    for category in dictionary:
        for book in dictionary[category]:
            if book["title"] == book_title:
                book_categories.add(category)
    category_count = 1
    for category in book_categories:
        print("Category " + str(category_count) + ": " + category)
        category_count += 1
    return len(book_categories)

#Test Functions
def test_get_books_by_publisher(tests_passed_failed:list)->list:
    
    """
    "Test get_books_by_publisher(test_dict, 'Crown Business')" checks if the function returns the expected result when the publisher indicated has only published one book from the dictionary.
    
    "Test get_books_by_publisher(test_dict, 'Simon and Schuster')" checks if the function returns the expected result when the publisher indicated has published multiple books from the dictionary.
    
    "Test get_books_by_publisher(test_dict, 'Billings Publishing')" checks if the function returns the expected result when the publisher indicated has not published any of the books in the dictionary.
    """
    
    tests_passed_failed = check_equal("Test get_books_by_publisher(test_dict, 'Crown Business')", get_books_by_publisher(test_dict, 'Crown Business'), 1, tests_passed_failed) 

    tests_passed_failed = check_equal("Test get_books_by_publisher(test_dict, 'Simon and Schuster')", get_books_by_publisher(test_dict, 'Simon and Schuster'), 4, tests_passed_failed)

    tests_passed_failed = check_equal("Test get_books_by_publisher(test_dict, 'Billings Publishing')", get_books_by_publisher(test_dict, 'Billings Publishing'), 0, tests_passed_failed)
    
    return tests_passed_failed

def test_get_all_categories_for_book_title(tests_passed_failed:list)->list:
    
    """
    "Test get_all_categories_for_book_title(all_books, 'The Painted Man (The Demon Cycle. Book 1)')" checks if the function returns the expected result when the book title in question is in multiple categories.
    
    "Test get_all_categories_for_book_title(all_books, 'Permanent Record')" checks if the function returns the expected result when the book title in question is in only one category.
    
    "Test get_all_categories_for_book_title(all_books, 'On the Origin of Species')" checks if the function returns the expected result when the book title in question is not in any category (ie, not in the dictionary at all).
    """
    
    tests_passed_failed = check_equal ("Test get_all_categories_for_book_title(all_books, 'The Painted Man (The Demon Cycle. Book 1)')", get_all_categories_for_book_title(all_books, 'The Painted Man (The Demon Cycle. Book 1)'), 3, tests_passed_failed) 
    
    tests_passed_failed = check_equal ("Test get_all_categories_for_book_title(all_books, 'Permanent Record')", get_all_categories_for_book_title(all_books, 'Permanent Record'), 1, tests_passed_failed) 

    tests_passed_failed = check_equal ("Test get_all_categories_for_book_title(all_books, 'On the Origin of Species')", get_all_categories_for_book_title(all_books, 'On the Origin of Species'), 0, tests_passed_failed)
    
    return tests_passed_failed
   

def test_get_books_by_category(tests_passed_failed:list)->list:
 """
 Return None and Print a "PASSED" message if actual and expected have same type and
 if they are equal otherwise it will print a "FAILED" message.
 >>>test_get_book_category() 
 The category Horror has 1 books. This is the list of books:
 Book 1 : The Mysterious Affair at Styles by Agatha Christie
 get_books_by_category Horror PASSED
 """ 
 tests_passed_failed = check_equal("get_books_by_category Horror",
                get_books_by_category(all_books,"Horror"),1,tests_passed_failed)

 tests_passed_failed = check_equal("get_books_by_category Fiction",
                get_books_by_category(all_books,"Fiction"),39,tests_passed_failed)

 tests_passed_failed = check_equal("get_books_by_category Comics",
                get_books_by_category(all_books,"Comics"),7, tests_passed_failed)
 return tests_passed_failed



def test_get_books_by_rate(tests_passed_failed:list)->list:
 """
 Return None and Print a "PASSED" message if actual and expected have same type and
 if they are equal otherwise it will print a "FAILED" message.
 >>>test_get_book_by_rate() 
 There are 13 books whose rate is between 5 and 6 . This is the list of books:
 Book 1 : Final Option: 'The best one yet' by Clive Cussler
 Book 2 : The Red Signal: An Agatha Christie Short Story by Agatha Christie
 Book 3 : Start Day Trading Now: A Quick and Easy Introduction to Making Money While Managing Your Risk by Michael Sincere
 ...
 get_books_by_rate 5<=rates<6 PASSED
 """  
 tests_passed_failed = check_equal("get_books_by_rate 3<=rates<4", get_books_by_rate(all_books,3),19, tests_passed_failed)
 tests_passed_failed = check_equal("get_books_by_rate 4<=rates<5",get_books_by_rate(all_books,4),152,tests_passed_failed)
 tests_passed_failed = check_equal("get_books_by_rate 5<=rates<6",get_books_by_rate(all_books,5),13,tests_passed_failed)
 return tests_passed_failed


def test_get_book_author(tests_passed_failed:list)->list:
    """
    Return None and Print a "PASSED" message if actual and expected have same type and
    if they are equal otherwise it will print a "FAILED" message.
    >>>test_get_book_author() 
    The author Peter V. Brett has published the following books:
    Book 1: The Painted Man (The Demon Cycle. Book 1), rate: 4.5
    get_books_by_author(book_category_dictionary("google_books_dataset.csv"),"Peter V. Brett") PASSED
    """
    tests_passed_failed = check_equal('get_books_by_author(book_category_dictionary("google_books_dataset.csv"),"Barbara Allan")',get_books_by_author(all_books,"Barbara Allan"),4, tests_passed_failed)
    tests_passed_failed = check_equal('get_books_by_author(book_category_dictionary("google_books_dataset.csv"),"Peter V. Brett")',get_books_by_author(all_books,"Peter V. Brett"),1, tests_passed_failed)
    tests_passed_failed = check_equal('get_books_by_author(book_category_dictionary("google_books_dataset.csv"),"Brandon Sanderson")',get_books_by_author(all_books,"Brandon Sanderson"),2, tests_passed_failed) 
    
    return tests_passed_failed

def test_get_books_by_title(tests_passed_failed:list)->list:
    """
    Return None and Print a "PASSED" message if actual and expected have same type and
    if they are equal otherwise it will print a "FAILED" message.
    >>>test_get_book_title() 
    The book has been found
    get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Con") PASSED
    """    
    tests_passed_failed = check_equal('get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Chop"',get_books_by_title(all_books,"Antiques Chop"),True, tests_passed_failed)
    tests_passed_failed = check_equal('get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques A Con")',get_books_by_title(all_books,"Antiques A Con"),False, tests_passed_failed)
    tests_passed_failed = check_equal('get_books_by_title(book_category_dictionary("google_books_dataset.csv"),"Antiques Con")',get_books_by_title(all_books,"Antiques Con"),True, tests_passed_failed)
    
    return tests_passed_failed


def test_add_book(tests_passed_failed:list)->list:
 """
 check_equal("add_book", add_book(test_dictionary_A_without_book, ("Harry Poter", "JK Rowling", 5.0, "The Publisher", 100, "Fiction", "English")), TEST_DICTIONARY_A_WITH_BOOK) Checks if a book in an existing category is added
 
 check_equal("add_book", add_book(test_dictionary_B_without_book, ("On the Origin of Species", "Charles Darwin", 4.0, "Simon and Schuster", 502, "Evolution", "English")), TEST_DICTIONARY_B_WITH_BOOK) Checks if a book in a not-yet-existing category is added
 
 check_equal("add_book", add_book(test_dictionary_C_1, ("title", "author", 1, "publisher", 1, "category2", "language")), TEST_DICTIONARY_C) Checks if a book already in the dictionary is added.
 """ 
 tests_passed_failed = check_equal("add_book", add_book(test_dictionary_A_without_book, ("Harry Poter", "JK Rowling", 5.0, "The Publisher", 100, "Fiction", "English")), TEST_DICTIONARY_A_WITH_BOOK, tests_passed_failed)
 tests_passed_failed = check_equal("add_book", add_book(test_dictionary_B_without_book, ("On the Origin of Species", "Charles Darwin", 4.0, "Simon and Schuster", 502, "Evolution", "English")), TEST_DICTIONARY_B_WITH_BOOK, tests_passed_failed)
 tests_passed_failed = check_equal("add_book", add_book(test_dictionary_C_1, ("title", "author", 1, "publisher", 1, "category2", "language")), TEST_DICTIONARY_C, tests_passed_failed) 
 return tests_passed_failed


def test_remove_book(tests_passed_failed:list)->list:
 """
 check_equal("remove_book", remove_book(test_dictionary_A_with_book, "Harry Poter", "Fiction"), TEST_DICTIONARY_A_WITHOUT_BOOK) Checks if a book in a larger category is removed
 
 check_equal("remove_book", remove_book(test_dictionary_B_with_book, "On the Origin of Species", "Evolution"), TEST_DICTIONARY_B_WITHOUT_BOOK) Checks if a book in a category by itself accidentally deletes that category entirely
 
 check_equal("remove_book", remove_book(test_dictionary_C_2, "nottitle", "category"), TEST_DICTIONARY_C) Checks if the function produces an error if a user tries to remove a book not in the database
 """ 
 tests_passed_failed = check_equal("remove_book", remove_book(test_dictionary_A_with_book, "Harry Poter", "Fiction"), TEST_DICTIONARY_A_WITHOUT_BOOK, tests_passed_failed)
 tests_passed_failed = check_equal("remove_book", remove_book(test_dictionary_B_with_book, "On the Origin of Species", "Evolution"), TEST_DICTIONARY_B_WITHOUT_BOOK, tests_passed_failed)
 tests_passed_failed = check_equal("remove_book", remove_book(test_dictionary_C_2, "nottitle", "category"), TEST_DICTIONARY_C, tests_passed_failed)
 return tests_passed_failed

# Main Script
if __name__ == "__main__":
 tests_passed_failed = [0 , 0]
 test_dict = book_category_dictionary("google_books_dataset.csv")
 all_books = book_category_dictionary("google_books_dataset.csv")
 tests_passed_failed = test_add_book(tests_passed_failed)
 tests_passed_failed = test_remove_book(tests_passed_failed)
 tests_passed_failed = test_get_books_by_category(tests_passed_failed)
 tests_passed_failed = test_get_books_by_rate(tests_passed_failed)
 tests_passed_failed = test_get_books_by_title(tests_passed_failed)
 tests_passed_failed = test_get_book_author(tests_passed_failed) 
 tests_passed_failed = test_get_books_by_publisher(tests_passed_failed)
 tests_passed_failed = test_get_all_categories_for_book_title(tests_passed_failed)