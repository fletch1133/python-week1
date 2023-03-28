### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here
def book_info():
    title = input('The Diary of Anne Frank')
    publication_year = input('1947')
    genre = input('Non-fiction')
    author = input('Anne Frank')
    language = input('Dutch')

book_dictionary {
    'title': The Dairy of Anne Frank,
    'publication_year': 1947,
    'genre': Non-fiction,
    'author': Anne Frank,
    'language': Dutch
}
return book_dictionary

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here
def book_info():
    title = input('Title: ')
    publication_year = int(input('Publication year: '))
    genre = input('Genre: ')
    author = input('Author: ')
    language = input('Language: ')


book_dictionary {
    'title': The Dairy of Anne Frank,
    'publication_year': 1947,
    'genre': Non-fiction,
    'author': Anne Frank,
    'language': Dutch
}

### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here
def book_info():
    title = input('title: ')
    while True:
        try:
            publication_year = int(input('Publication year: '))
            break
        except ValueError:
            print("What year was the book published in?")
    genre = input('Genre: ')
    author = input('Author: ')
    language = input('Language: ')

    book_dictionary = {
        'title': title,
        'publication_year': publication_year,
        'genre': genre,
        'author': author,
        'language': language
    }

    return book_dictionary



### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here
def main_menu():
    while True:
        print("Please choose an option:")
        print("1. Add a new book")
        print("2. Leave")

        choice = input("Enter your decision (1 or 2): ")

        if choice == "1":
            book = book_info()
            print("The book was added successfully!")
            print(book)
        elif choice == "2":
            print("Thank you for visiting!")
            break
        else:
            print("Incorrect selection. Please choose again!")
### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here
def main_menu():
    while True:
        print("Please choose an option:")
        print("1. Add a new book")
        print("2. Leave")

        choice = input("Enter your decision (1 or 2): ")

        if choice == "1":
            book = book_info()
            print("The book was added successfully!")
            print(book)
        elif choice == "2":
            print("Thank you for visiting!")
            break
        else:
            print("Incorrect selection. Please choose again!")

            print("Exited main menu.")

main_menu()