# Milestone 3 P5 Task 1
#Ali Abdollahian 101229396
#Daniele Caruso 101220647
#Yancheng Ding 101223452
#Keegan Kilfoil 101220476
#2022-04-11
#Version 1.0

import string
from typing import List

def book_category_dictionary(filename)->dict[str:str]:
    """
    Returns a dictionary with the stored data based on the category of file google_books_dataset.csv as filename 
    >>>book_category_dictionary("google_books_dataset.csv")
    {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'pages': 288, 'category': 'Fiction', 'language': 'English\n'},...]}
    """
    all_books={}
    dataset = open(filename, "r")
    count = 0
    for line in dataset:
        count += 1
        line = line.replace('\n', '')
        values = line.split(",")
        if count == 1:
            key1 = values[0]
            key2 = values[1]
            key3 = values[2]
            key4 = values[3]
            key5 = values[4]
            key6 = values[5]
            key7 = values[6]
        else:
            data_dic = {}
            data_dic[key1] = values[0]
            data_dic[key2] = values[1]
            if values[2] != ("N/A"):
                data_dic[key3] = float(values[2])
            else:
                data_dic[key3] = values[2]
            data_dic[key4] = values[3]
            data_dic[key5] = int(values[4])
            data_dic[key6] = values[5]
            data_dic[key7] = values[6]
            if not values[5] in all_books:
                all_books[values[5]] = []
            all_books[values[5]] += [data_dic]
    for category in all_books:
        booklist = (all_books[category])
        index_book_a = 0
        index_book_b = 0
        for book_a in booklist:
            index_book_a += 1
            for book_b in booklist:
                index_book_b += 1
                if book_b['title'] == book_a['title'] and index_book_a != index_book_b:
                    booklist.remove(book_b)
            index_book_b = 0
    return all_books

if __name__ == "__main__":
    print(book_category_dictionary("google_books_dataset.csv"))