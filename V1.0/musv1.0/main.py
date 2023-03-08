"""
Music Library Software
version : 1.0.0

RELEASE NOTES: 
CLI Program that lets you store songs that you like in a list inside of a .txt file
in this case titled 'SongList.txt'

*** entries in this program are not stored in a database (see v3.0) ***

"""



def main():
    
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
    
    choice = 0 # User Input
    while choice !=4:
        print("--- MUSIC LIBRARY MANAGEMENT SYSTEM V1.0 ---")
        print("--- By Mizakson ---")
        print("1. ADD A SONG")
        print("2. LOOKUP A SONG")
        print("3. DISPLAY SONGS")
        print("4. QUIT")
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
            print("CLOSING PROGRAM...")
    print("PROGRAM TERMINATED")
    
    # Saving to external TXT file
    outfile = open("SongList.txt", "w")
    for song in songsList:
        outfile.write(", ".join(song) + "\n")
    outfile.close()
                    


if __name__ == "__main__":
    main()