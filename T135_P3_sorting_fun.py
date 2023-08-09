# ECOR 1042 Group Project Milestone2 Lab1 P3 Sorting group code 
#Ali Abdollahian 101229396
#Daniele Caruso 101220647
#Yancheng Ding 101223452
#Keegan Kilfoil 101220476
#2022-04-11
#Version 1.0

import string
from typing import List
from T135_check_equal import check_equal

def dictionary_to_list(data:dict)->list:
    lst=[]
    for category in data.keys():
        books=data.get(category)
        for i in range(len(books)):
            books[i]['category']=[category]
        if len(lst)==0:
            lst=books
        else:
            for book in books:
                book_lst = False
                for i in range(len(lst)):
                    if book['title']==lst[i]['title']:
                        lst[i]['category']+=book['category']                    
                        book_lst=True
                if book_lst==False:
                    lst+=[book]  
    return lst
    
def sort_books_title(data:dict)->list:
    """
    Returns a list of books data which each element is a dictionary containing the data of books also
    they are sorted by their title alphabetic order using bubble method by giving it books dataset as data
    >>>sort_books_title(book_category_dictionary("google_books_dataset.csv"))
    [{'title': "'Salem's Lot", 'author': 'Stephen King', 'rating': 4.4, 'publisher': 'Hachette UK', 'pages': 300, 'category': ['Fiction', 'Thrillers'], 'language': 'English\n'}, {'title': 'A Feast for Crows (A Song of Ice and Fire. Book 4)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 864, 'category': ['Fiction', 'Fantasy', 'Adventure', 'Epic'], 'language': 'English\n'},...]
    """
    lst = dictionary_to_list(data)
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]['title'] > lst[j]['title'] :
                lst[i], lst[j] = lst[j], lst[i]    
    return lst

def sort_books_author (dict: dict) -> list[dict]:  
    """
    Precondition: The dictionary used as the argument must be of the form
    returned by the function book_category_dictionary.
    
    Returns a list of the books within dict stored in alphabetical order by
    author name. If multiple books have been written by the same author, those
    books are sorted alphabetically by title. Each book is stored as a
    dictionary within the list.
    
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}], 'Information Technology': [{'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': 'Information Technology', 'language': 'English\n'}], 'Detective': [{'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': ['Detective'], 'language': 'English\n'}], 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Investing', 'language': 'English\n'}]}
    
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Alvin Hall', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Barbara Allan', 'rating': 4.6, 'publisher': 'Crown Business', 'pages': 464, 'category': ['Information Technology'], 'language': 'English\n'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 240, 'category': ['Detective'], 'language': 'English\n'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Brent Schlender', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': ['Investing'], 'language': 'English\n'}]
    
    """
    book_list = dictionary_to_list(dict)
    n = len(book_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if book_list[j]["author"] > book_list[j+1]["author"]:
                hold = book_list[j]
                book_list[j] = book_list[j+1]
                book_list[j+1] = hold                
            if book_list[j]["author"] == book_list[j+1]["author"]:
                if book_list[j]["title"] > book_list[j+1]["title"]:
                    hold = book_list[j]
                    book_list[j] = book_list[j+1]
                    book_list[j+1] = hold                                  
    return book_list

def sort_books_publisher(database:dict) -> list:
    """
    Returns a list of all books in the dictionary sorted alphabetically by publisher. If the books have the same publisher,
    they are sorted alphabetically by title. If the book is in multiple categories, the category key will contain a list of 
    categories the book is in.
    
    Precondition: Database must be a dictionary with book categories as keys. The categories should contain a list of books, 
    with each book in the database being a dictionary with atleast one key: 'publisher'.
    
    sort_books_publisher({'category1': [{'title': 'book1', 'publisher': 'b_publisher'}, {'title': 'book2', 'publisher': 'a_publisher'}]})
    [{'title': 'book2', 'publisher': 'a_publisher', 'category': 'category1'}, {'title': 'book1', 'publisher': 'b_publisher', 'category': 'category1'}]
    
    sort_books_publisher({'category1': [{'title': 'book1', 'publisher': 'a_publisher'}, {'title': 'book1', 'publisher': 'a_publisher'}]})
    [{'title': 'book1', 'publisher': 'a_publisher', 'category': 'category1'}]
    
    sort_books_publisher({'category1': [{'title': 'book1', 'publisher': 'b_publisher'}, {'title': 'book2', 'publisher': 'a_publisher'}], category2: [{'title': 'book1', 'publisher': 'b_publisher'}]})
    [{'title': 'book2', 'publisher': 'a_publisher', 'category': 'category1'}, {'title': 'book1', 'publisher': 'b_publisher', 'category': ['category1', 'category2']}]
    """
    
    booklist = dictionary_to_list(database)
    for book in range(len(booklist)):
        for entry in range(len(booklist)-book-1):
            if booklist[entry]['publisher'] > booklist[entry+1]['publisher']:
                temporary = booklist[entry]
                booklist[entry] = booklist[entry+1]
                booklist[entry+1] = temporary
            elif booklist[entry]['publisher'] == booklist[entry+1]['publisher'] and booklist[entry]['title'] > booklist[entry+1]['title']:
                temporary = booklist[entry]
                booklist[entry] = booklist[entry+1]
                booklist[entry+1] = temporary                
    return booklist

def sort_books_ascending_rate(data:dict)->list:
    """
    Returns a list of dictionaries containing books that are arranged in ascending
    order of ratings, where all books are from the given dictionary.
    >>>sort_books_ascending_rate(book_category_dictionary("google_books_dataset.csv"))
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 
      'author': 'Brian Tracy', 
      'language': 'English', 
      'rating': 'N/A', 
      'publisher': 'AMACOM', 
      'category': ['Economics', 'Business'], 
      'pages': 112}
      ...
     {'title': 'The Red Signal: An Agatha Christie Short Story', 
      'author': 'Agatha Christie', 
      'language': 'English', 
      'rating': 5.0, 
      'publisher': 'HarperCollins UK', 
      'category': ['Fiction', 'Detective', 'Mystery', 'Traditional'], 
      'pages': 40}
      ]
    """
    books=dictionary_to_list(data)
    n=len(books)
    for i in range(n):
        for j in range(n-i-1):
            score_one=books[j].get('rating')
            score_two=books[j+1].get('rating')
            if score_one=="N/A":
                score_one=0
            if score_two=="N/A":
                score_two=0
            if score_one>score_two:
                books[j],books[j+1]=books[j+1],books[j]
            if books[j].get('rating')==books[j+1].get('rating'):
                if books[j].get('title')>books[j+1].get('title'):
                    books[j],books[j+1]=books[j+1],books[j]
    return books
    

test_dictionary_expected=[{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': ['Fiction'], 'language': 'English\n'}]

test_condition_1={'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'pages': 336, 'category': 'Fiction', 'language': 'English\n'}]}

def test_sort_books_ascending_rate(tests_passed_failed:list):
    """
    Return None and Print a "PASSED" message if actual and expected have same type and
    if they are equal otherwise it will print a "FAILED" message.
    also it is not to be used to check for floats, lists of floats,
    tuples of floats, etc. are equal.
    description is a string to help us about what is test
    >>>test_sort_books_ascending_rate()
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}...]
    """
    tests_passed_failed = check_equal("Test sort_books_ascending_rate",sort_books_ascending_rate(test_condition_1),test_dictionary_expected,tests_passed_failed)
    return tests_passed_failed

test_dict = {'Fiction': [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': 'Fiction', 'language': 'English\n'}], 'Investing': [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': 'Investing', 'language': 'English\n'}], "Thriller": [{'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Thriller', 'language': 'English\n'}]} 

def test_sort_books_publisher(tests_passed_failed:list) -> None:
    
    """
    Test sort_books_publisher(test_dict) checks if the function returns a list with the books in alphabetical order by publisher name. This test also verifies that when multiple books of the same publisher are in the argument dictionary, the function orders those books alphabetically by title. The test also verifies that when a book belongs to multiple categories, the value paired with the "category" key will be a list of the categories that the book in question belongs to.
    """
    
    tests_passed_failed = check_equal ("Test sort_books_publisher(test_dict)", sort_books_publisher(test_dict),  [{'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': 3.7, 'publisher': 'Hachette UK', 'pages': 30, 'category': ['Investing'], 'language': 'English\n'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'pages': 416, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': ['Fiction', 'Thriller'], 'language': 'English\n'}],tests_passed_failed)

    return tests_passed_failed

TEST_DICT_A = {'category1': [{'title': 'book1', 'author': 'b_author', 'category': 'category1'}, {'title': 'book2', 'author': 'c_author', 'category': 'category1'}, {'title': 'book3', 'author': 'a_author', 'category': 'category1'}]}
TEST_DICT_A_SORTED = [{'title': 'book3', 'author': 'a_author', 'category': ['category1']}, {'title': 'book1', 'author': 'b_author', 'category': ['category1']}, {'title': 'book2', 'author': 'c_author', 'category': ['category1']}]
TEST_DICT_B = {'category1': [{'title': 'book1', 'author': 'b_author', 'category': 'category1'}, {'title': 'book2', 'author': 'c_author', 'category': 'category1'}], 'category2': [{'title': 'book3', 'author': 'a_author', 'category': 'category2'}]}
TEST_DICT_B_SORTED = [{'title': 'book3', 'author': 'a_author', 'category': ['category2']}, {'title': 'book1', 'author': 'b_author', 'category': ['category1']}, {'title': 'book2', 'author': 'c_author', 'category': ['category1']}]
TEST_DICT_C = {'category1': [{'title': 'book1', 'author': 'b_author', 'category': 'category1'}, {'title': 'book2', 'author': 'c_author', 'category': 'category1'}], 'category2': [{'title': 'book3', 'author': 'a_author', 'category': 'category2'}, {'title': 'book1', 'author': 'b_author', 'category': 'category2'}]}
TEST_DICT_C_SORTED = [{'title': 'book3', 'author': 'a_author', 'category': ['category2']}, {'title': 'book1', 'author': 'b_author', 'category': ['category1', 'category2']}, {'title': 'book2', 'author': 'c_author', 'category': ['category1']}]

#Test Function
def test_sort_books_author(tests_passed_failed:list) -> None:
    
    """
    Tests the function sort_books_author()
    
    "Test test_sort_books_author(TEST_DICT_A)" checks if the function returns the expected result when presented with a straightforward dictionary
    
    "Test test_sort_books_author(TEST_DICT_B)" checks if the function returns the expected result when multiple categories are present

    "Test test_sort_books_author(TEST_DICT_B)" checks if the function returns the expected result when multiple categories are present and a book is in more than one category
    """
    
    tests_passed_failed = check_equal("Test test_sort_books_author(TEST_DICT_A)", str(sort_books_author(TEST_DICT_A)), str(TEST_DICT_A_SORTED),tests_passed_failed) 
    
    tests_passed_failed = check_equal("Test test_sort_books_author(TEST_DICT_B)", str(sort_books_author(TEST_DICT_B)), str(TEST_DICT_B_SORTED),tests_passed_failed)
    
    tests_passed_failed = check_equal("Test test_sort_books_author(TEST_DICT_C)", str(sort_books_author(TEST_DICT_C)), str(TEST_DICT_C_SORTED),tests_passed_failed)
    
    return tests_passed_failed

dictionary_title_one={'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'pages': 544, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'pages': 226, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'pages': 400, 'category': 'Fiction', 'language': 'English\n'}], 'Comics': [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'pages': 96, 'category': 'Comics', 'language': 'English\n'}]}

dictionary_title_two={'Humor': [{'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': 'Humor', 'language': 'English\n'}], 'Fiction': [{'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': 'Fiction', 'language': 'English\n'}], 'Fantasy': [{'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': 'Fantasy', 'language': 'English\n'}]}

def test_sort_books_title(tests_passed_failed:list)->None:
    #Test 1
    tests_passed_failed = check_equal("sort_books_title",sort_books_title(dictionary_title_one),[{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English\n', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'category': ['Fiction'], 'pages': 288}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English\n', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'category': ['Comics'], 'pages': 96}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Tor Books', 'category': ['Fiction'], 'pages': 226}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English\n', 'rating': 4.8, 'publisher': 'Hachette UK', 'category': ['Fiction'], 'pages': 400}, {'title': 'The Painted Man (The Demon Cycle. Book 1)', 'author': 'Peter V. Brett', 'language': 'English\n', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'category': ['Fiction'], 'pages': 544}],tests_passed_failed)
    #Test 2
    tests_passed_failed = check_equal("sort_books_title",sort_books_title(dictionary_title_two), [{'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': 4.5, 'publisher': 'Kensington Books', 'pages': 240, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': 4.8, 'publisher': 'Kensington Books', 'pages': 288, 'category': ['Fiction'], 'language': 'English\n'}, {'title': 'Tall Tales and Wee Stories: The Best of Billy Connolly', 'author': 'Billy Connolly', 'rating': 5.0, 'publisher': 'Hachette UK', 'pages': 336, 'category': ['Humor'], 'language': 'English\n'}, {'title': 'The Name of the Wind: The Kingkiller Chronicle:Book 1', 'author': 'Patrick Rothfuss', 'rating': 4.3, 'publisher': 'Hachette UK', 'pages': 672, 'category': ['Fantasy'], 'language': 'English\n'}],tests_passed_failed)
    
    return tests_passed_failed
    
# Main script 
if __name__=='__main__':
    tests_passed_failed = [0,0]
    tests_passed_failed=test_sort_books_title(tests_passed_failed)
    tests_passed_failed=test_sort_books_author(tests_passed_failed)
    tests_passed_failed=test_sort_books_publisher(tests_passed_failed)
    tests_passed_failed=test_sort_books_ascending_rate(tests_passed_failed)

    
