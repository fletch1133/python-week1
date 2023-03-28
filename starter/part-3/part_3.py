my_book = {
    "title": "Then Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}

# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below
def format_book_info(book_dict):
    title = book_dict['title']
    author = book_dict['author']
    year = book_dict['year']
    rating = book_dict['rating']
    pages = book_dict['pages']

    return f"{title} by {author}, was published in the {year}. The {rating} of the book is highest among its peers and has a total of {pages} pages."





# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below
def get_book_title(book_dict):
    return book_dict['title']

def get_book_author(book_dict):
    return book_dict['author']

def get_book_year(book_dict):
    return book_dict['year']

def get_book_rating(book_dict):
    return book_dict['rating']

def get_book_pages(book_dict):
    return book_dict['pages']


# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps thing of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below
my_fav_book = {
    "title": "The Art of Racing in the Rain",
    "author": "Garth Stein",
    "year": 2008,
    "rating": 4.20,
    "pages": 336
}

def search_books_by_author(books, author):
    return [book for book in books if book['author'] == author]

def get_highest_rated_book(books):
    return max(books, key=lambda x: x['rating'])

def calculate_total_pages(books):
    return sum(book['pages'] for book in books)

