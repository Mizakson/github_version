"""
Media Library Management Software
version : 3.0

RELEASE NOTES:
CLI Program that stores books and songs in an sqlite3 database

ADDED FEATURES:

Database connectivity
    - sqlite3 database with two tables, one for books and one for songs

Implementaion of CRUD functionality
    - can perform CRUD operations on both tables

Update Function
    - can update a book's read status (Y or N)
    - can update a song's genre

sys module
    - added sys.exit() instead of break

User input converted to all uppercase using .upper()

"""
import sys
import sqlite3

# Connect to database
conn = sqlite3.connect('media_library.db') # insert your db name here

# Cursor object
c = conn.cursor()


"""BOOK LIBRARY SECTION
CRUD FUNCTIONS, SQLite db connection and cursor object
"""


# Execute a CREATE TABLE statement to create the "books" table
c.execute('''CREATE TABLE IF NOT EXISTS books
             (Title TEXT,
              Author TEXT,
              Read TEXT,
              Genre TEXT)''')

# Function to insert a new book into the database
def insert_book(title, author, read, genre):
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (title, author, read, genre))
    conn.commit()
    print("BOOK ADDED SUCCESSFULLY.")

# Function to read all books from the database
def read_books():
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for book in books:
        print(book)


# Function to update whether a book has been read
def update_book_read(title, author, read):
    c.execute("UPDATE books SET Read=? WHERE Title=? AND Author=?", (read, title, author))
    conn.commit()
    print("BOOK UPDATED SUCCESSFULLY.")
        

# Function to delete a book from the database
def delete_book(title, author):
    c.execute("DELETE FROM books WHERE Title=? AND Author=?", (title, author))
    conn.commit()
    print("BOOK DELETED SUCCESSFULLY.")




# book library main function
def booklib():
    while True:
        print("--- LIBRARY MANAGEMENT SYSTEM V3.0 ---")
        print("1. ADD A BOOK")
        print("2. VIEW ALL BOOKS")
        print("3. UPDATE A BOOK'S READ STATUS")
        print("4. DELETE A BOOK")
        print("5. RETURN TO MAIN MENU")
        print("6. QUIT")
        print("A program by Mizakson")
        choice = int(input("ENTER OPTION HERE: "))
            
        if choice == 1:
            title = input("ENTER BOOK TITLE: ").upper()
            author = input("ENTER AUTHOR NAME: ").upper()
            read = input("HAVE YOU READ THIS BOOK BEFORE? (Y/N): ").upper()
            genre = input("ENTER GENRE: ").upper()
            insert_book(title, author, read, genre)

        elif choice == 2:
            read_books()

        elif choice == 3:
            title = input("ENTER BOOK TITLE: ").upper()
            author = input("ENTER AUTHOR NAME: ").upper()
            read = input("HAVE YOU READ THIS BOOK BEFORE? (Y/N): ").upper()
            update_book_read(title, author, read)

        elif choice == 4:
            title = input("ENTER BOOK TITLE: ").upper()
            author = input("ENTER AUTHOR NAME: ").upper()
            delete_book(title, author)

        elif choice == 5:
            break

        elif choice == 6:
            sys.exit("PROGRAM TERMINATED")

        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")



"""MUSIC LIBRARY SECTION
CRUD FUNCTIONS, SQLite db connection and cursor object
"""



# Execute a CREATE TABLE statement to create the "songs" table
c.execute('''CREATE TABLE IF NOT EXISTS songs
             (name TEXT,
              artist TEXT,
              genre TEXT)''')


# Function to insert a new song into the database
def insert_song(name, artist, genre):
    c.execute("INSERT INTO songs VALUES (?, ?, ?)", (name, artist, genre))
    conn.commit()
    print("SONG ADDED SUCCESSFULLY.")

# Function to read all songs from the database
def read_songs():
    c.execute("SELECT * FROM songs")
    songs = c.fetchall()
    for song in songs:
        print(song)

# Function to update the genre of an existing song
def update_song_genre(name, artist, new_genre):
    c.execute("UPDATE songs SET genre=? WHERE name=? AND artist=?", (new_genre, name, artist))
    conn.commit()
    print("SONG UPDATED SUCCESSFULLY.")

# Function to delete a song from the database
def delete_song(name, artist):
    c.execute("DELETE FROM songs WHERE name=? AND artist=?", (name, artist))
    conn.commit()
    print("SONG DELETED SUCCESSFULLY.")


def musiclib():  
    
    # Prompt the user for input and call the appropriate CRUD function
    while True:
        print("--- MUSIC LIBRARY MANAGEMENT SYSTEM V3.0 ---")
        print("1. ADD A SONG")
        print("2. VIEW ALL SONGS")
        print("3. UPDATE A SONG'S GENRE")
        print("4. DELETE A SONG")
        print("5. RETURN TO MAIN MENU")
        print("6. QUIT")
        print("A program by Mizakson")
        choice = int(input("ENTER OPTION HERE: "))

        if choice == 1:
            name = input("ENTER SONG NAME: ").upper()
            artist = input("ENTER ARTIST NAME: ").upper()
            genre = input("ENTER GENRE: ").upper()
            insert_song(name, artist, genre)
        
        elif choice == 2:
            read_songs()
        
        elif choice == 3:
            name = input("ENTER SONG NAME: ").upper()
            artist = input("ENTER ARTIST NAME: ").upper()
            genre = input("ENTER GENRE: ").upper()
            update_song_genre(name, artist, genre)
        
        elif choice == 4:
            name = input("ENTER SONG NAME: ").upper()
            artist = input("ENTER ARTIST NAME: ").upper()
            delete_song(name, artist)
        
        elif choice == 5:
            break
        
        elif choice == 6:
            sys.exit("PROGRAM TERMINATED")
        
        else:
            print("INVALID CHOICE. PLEASE TRY AGAIN.")



# homepage section
def home_page():
    while True:
        print("--- PERSONAL MEDIA LIBRARY MANAGEMENT SYSTEM HOMEPAGE V3.0 ---")
        print("1. GO TO BOOK LIBRARY ")
        print("2. GO TO MUSIC LIBRARY ")
        print("3. QUIT ")
        print("A program by Mizakson")
        choice = int(input("ENTER OPTION HERE: "))
        
        if choice == 1:
            print("GOING TO BOOK LIBRARY... ")
            booklib()
        
        elif choice == 2:
            print("GOING TO MUSIC LIBRARY... ")
            musiclib()
        
        elif choice == 3:
            print("CLOSING PROGRAM...")
            print("THANKS FOR VISITING :)")
            sys.exit()      
        
        else:
            print("ENTER A VALID OPTION... ")


# initialize homepage function to start the program
if __name__ == "__main__":
    home_page()