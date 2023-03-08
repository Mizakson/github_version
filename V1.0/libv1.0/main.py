"""
Book Library Software
version : 1.0

RELEASE NOTES: 
CLI Program that lets you store books in a list inside of a .txt file
in this case titled 'BookList.txt'

*** entries in this program are not stored in a database (see v3.0) ***

"""


def main():
    
    try:    
        # initialize books list
        booksList = []
        infile = open("BookList.txt", "r")
        line = infile.readline()
        while line:
            booksList.append(line.rstrip("\n").split(",") )
            line = infile.readline()
        infile.close()
        
    except FileNotFoundError : # error shown if there is no BookList.txt file 
        print("THE <BookList.txt> FILE IS NOT FOUND ")
        print("STARTING A NEW BOOK LIST...")
        booksList = []    
    
    choice = 0 # User Input
    while choice !=4:
        print("--- LIBRARY MANAGEMENT SYSTEM V1.0 ---")
        print("--- By Mizakson ---")
        print("1. ADD A BOOK")
        print("2. LOOKUP A BOOK")
        print("3. DISPLAY BOOKS")
        print("4. QUIT")
        choice = int(input())
        
        if choice == 1:
            print("ADDING BOOK...")
            nBook = input("ENTER BOOK TITLE >>> ")
            nAuthor = input("ENTER AUTHOR NAME >>> ")
            rBefore = input("HAVE YOU READ IT BEFORE ? >>> ")
            nGenre = input("ENTER GENRE >>> ")
            booksList.append([nBook, nAuthor, rBefore, nGenre])
        
        elif choice == 2:
            print("LOOKING UP A BOOK...")
            keyword = input("ENTER TITLE: ")
            for book in booksList:
                if keyword in book:
                    print(book)
        
        elif choice == 3:
            print("DISPLAYING ALL BOOKS...")
            for i in range(len(booksList)):
                print(booksList[i])
        
        elif choice == 4:
            print("CLOSING PROGRAM...")
    print("PROGRAM TERMINATED")
    
    # Saving to external TXT file
    outfile = open("BookList.txt", "w")
    for book in booksList:
        outfile.write(", ".join(book) + "\n")
    outfile.close()
                    


if __name__ == "__main__":
    main()