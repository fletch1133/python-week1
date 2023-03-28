### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here
def add_book_to_file(title, author, publication_year, filename):
    with open(filename, 'a') as file:
        file.write(f'{title}, {author}, {publication_year}\n')


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here
def print_books_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            title, author, publication_year = line.strip().split(', ')
            print(f'Title: {title}, Author: {author}, Publication_Year: {publication_year}')


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script

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
if __name__ == '__main__':
main_menu()

### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

