"""
Media Library Management Software
version : 2.0.0

RELEASE NOTES: 
CLI Program that lets you store songs and books 
in separate lists in individual .txt files

ADDED FEATURES:
home_page function
    - main menu allowing you to go to either program or exit

"""

def booklib():
        
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
        
    
    while True:
        print("--- LIBRARY MANAGEMENT SYSTEM V2.0 ---")
        print("--- By Mizakson ---")
        print("1. ADD A BOOK")
        print("2. LOOKUP A BOOK")
        print("3. DISPLAY BOOKS")
        print("4. RETURN TO HOMEPAGE")
        print("5. QUIT")
        choice = int(input("ENTER OPTION HERE: "))
            
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
            print("RETURNING TO HOMEPAGE... ")
            return

        elif choice == 5:
            print("CLOSING PROGRAM...")
            print("THANKS FOR VISITING :)")
            break

        else:
            print("ENTER A VALID OPTION... ")
    
    # Saving to external TXT file
    outfile = open("BookList.txt", "w")
    for book in booksList:
        outfile.write(", ".join(book) + "\n")
    outfile.close()


def musiclib():
        
    try:    
    # initialize songs list
        songsList = []
        infile = open("SongList.txt", "r")
        line = infile.readline()
        while line:
            songsList.append(line.rstrip("\n").split(",") )
            line = infile.readline()
        infile.close()
            
    except FileNotFoundError : # error shown if there is no SongList.txt file 
        print("THE <SongList.txt> FILE IS NOT FOUND ")
        print("STARTING A NEW SONG LIST...")
        songsList = []    
    
    while True:
        print("--- MUSIC LIBRARY MANAGEMENT SYSTEM V2.0 ---")
        print("1. ADD A SONG")
        print("2. LOOKUP A SONG")
        print("3. DISPLAY SONGS")
        print("4. RETURN TO HOMEPAGE")
        print("5. QUIT")


        choice = int(input())       
        if choice == 1:
            print("ADDING SONG...")
            nSong = input("ENTER SONG NAME >>> ")
            nArtist = input("ENTER ARTIST NAME >>> ")
            nGenre = input("ENTER GENRE >>> ")
            songsList.append([nSong, nArtist, nGenre])
            
        elif choice == 2:
            print("LOOKING UP A SONG...")
            keyword = input("ENTER SONG NAME: ")
            for song in songsList:
                if keyword in song:
                    print(song)
        
        elif choice == 3:
            print("DISPLAYING ALL SONGS...")
            for i in range(len(songsList)):
                print(songsList[i])
            
        elif choice == 4:
            print("RETURNING TO HOMEPAGE... ")
            return
            
        elif choice == 5:
            print("CLOSING PROGRAM...")
            print("THANKS FOR VISITING :)")
            break

        else:
            print("ENTER A VALID OPTION... ")
        
    # Saving to external TXT file
        outfile = open("SongList.txt", "w")
        for song in songsList:
            outfile.write(", ".join(song) + "\n")
        outfile.close()

def main_menu():
    while True:
        print("--- PERSONAL MEDIA LIBRARY MANAGEMENT SYSTEM HOMEPAGE ---")
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
            break       
        else:
            print("ENTER A VALID OPTION... ")


# initialize main function
if __name__ == "__main__":
    main_menu()