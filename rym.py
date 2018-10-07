#! /usr/bin/env python3

"""
This program searches rym based on certain arguments

Unfortunately, you cannot make requests on 
rym––they will block you. So some things that could
easily be done by first making a request to check if
it returns a 404 is not possible. 

Input Info:
    Write '&'' as and 
    Don't include apostrophes or accent marks
    Seperate hypenated words: wu-tang clan entered as wu tang clan !!UNLESS IT'S A GENRE NAME
Usage: 
    Artist Search: rym.py names of artist/band seperated by spaces
    Film Search: rym.py film name of film seperated by spaces
    Album Search: rym.py album name of album seperated by spaces -- artist name sep by spaces(THIS WILL ONLY WORK FOR FULL LENGTHS)
    Genre Search: rym.py genre name of genre seperated by spaces
    Year Search: rym.py year yearDate (search by decade by adding s at end. Example: 1990s)
    Top Albums of All Time: rym.py top
    Top Films of All Time: rym.py topfilms

    **Adding more search terms is not worth the effort of automating**

    TODO:
    Remove mutated variables
    DOCUMANTATION IT UP
"""
import sys, webbrowser

#--------Display Help Menu---------------------
# Called when --help is entered
# Essentially just the githup README.md
def helpMenu():
    print("""
Artist Search: rym.py name of artist/band seperated by spaces
    * Brings user to entered artist's page.
    * Example: rym.py my bloody valentine

Film Search: rym.py film name of film seperated by spaces
    * Brings user to entered film's page.
    * Example: rym.py film eternal sunshine of the spotless mind

Album Search: rym.py album name of album seperated by spaces -- artist name seperated by spaces
    * Brings user to entered album's page.
    * Example: rym.py album my beautiful dark twisted fantasy -- kanye west
    * ONLY WORKS FOR FULL LENGTH ALBUMS

Genre Search: rym.py genre name of genre seperated by spaces
    * Brings user to top of all time list for entered genre.
    * Example: rym.py genre progressive rock
    * Some genres require punctuation
        * Example: rym.py genre post-punk

Year Search: rym.py year yearDate
    * Brings user to top of all time for given year.
    * Example: rym.py year 1977
    * You can also search by decade
        Example: rym.py year 1980s

Top Albums of All Time: rym.py top
    * Brings user to overall top of all time for albums.

Top Films of All Time: rym.py topfilms
    * Brings user to overall top of all time for films.

RYM Home Page: rym.py
    * Brings user to rateyourmusic.com.

General Input Info:
    * Write '&'' as and 
    * Don't include apostrophes or accent marks
    * Seperate hypenated words: 
        * Wu-Tang clan as wu tang clan 
        * Include hyphens if genre searching
        """)
#---------------------------------

#-------Check and Edit Input---------
# Removes certain characters from input that rym doesn't like
def checkValid(userInput):
    # Punctuations that make rym mad
    problemPunctuations = (':', ',', '.', '!', '?')

    # Remove the problems
    for puncType, punct in enumerate(problemPunctuations):
        # Check if there are any problems in input
        while problemPunctuations[puncType] in userInput:
            problemCharIndex = userInput.index(punct)   # holds index with the unsupported punct
            # If '!' or '?' just remove it
            if puncType == '!' or puncType == '?':
                fixedInput = userInput[:problemCharIndex] + userInput[problemCharIndex+1:]
            # Other wise replace punt with a '_'
            else:
                fixedInput = userInput[:problemCharIndex] + "_" + userInput[problemCharIndex+1:]

    return fixedInput
#------------------------------------

#---Specific Search Link Functions---------
# Create the proper url
def searchYear(greatYear):
    urlYear = f'https://rateyourmusic.com/charts/top/album/{greatYear}'
    return urlYear

def searchGenre(engagingGenre):
    urlGenre = f'https://rateyourmusic.com/customchart?page=1&chart_type=top&type=album&year=alltime&genre_include=1&genres={engagingGenre}&include_child_genres=t&include=both&limit=none&countries='
    return urlGenre

def searchAlbum(sickAlbum, coolArtist):
    coolArtist = checkValid(coolArtist)
    sickAlbum = checkValid(sickAlbum)
    urlAlbum = f'https://rateyourmusic.com/release/album/{coolArtist}/{sickAlbum}'
    return urlAlbum

def searchFilm(funFilm):
    funFilm = checkValid(funFilm)
    urlFilm = f'https://rateyourmusic.com/film/{funFilm}'
    return urlFilm

def searchArtist(coolArtist):
    if coolArtist == "toto":
        webbrowser.open('https://www.youtube.com/watch?v=FTQbiNvZqaY')
    coolArtist = checkValid(coolArtist)
    urlArtist = f'https://rateyourmusic.com/artist/{coolArtist}'
    return urlArtist
#--------------------------------

#---Determine What User Wants to Search Then Open Browser----
def searchRym():
    if len(sys.argv) > 1:
        # Search by film
        if (sys.argv[1] == "film"):
            film = '_'.join(sys.argv[2:])
            lowerFilm = film.lower()
            search = searchFilm(lowerFilm)
        # Give top of all time films
        elif (sys.argv[1] == "topfilms"):
            search = "https://rateyourmusic.com/films/chart"
        # Give top of all time chart for a given genre
        elif (sys.argv[1] == "genre"):
            genre = '+'.join(sys.argv[2:])
            search = searchGenre(genre)
        # Give top albums of given year (or decade)
        elif (sys.argv[1] == "year"):
            year = sys.argv[2]
            search = searchYear(year)
        # Search by album
        elif (sys.argv[1] == "album"):
            album = ' '.join(sys.argv[2:])
            split = album.split('--')
            print(split)
            album = split[0]
            album = album.split()
            album = '_'.join(album)
            lowerAlbum = album.lower()

            artist = split[1]
            artist = artist.split()
            artist = '_'.join(artist)
            lowerArtist = artist.lower()

            search = searchAlbum(lowerAlbum, lowerArtist)
        # Top of all time
        elif (sys.argv[1] == "top"):
            search = "https://rateyourmusic.com/customchart"
        elif (sys.argv[1] == "--help"):
            helpMenu()
            sys.exit()
        else:
            artist = '_'.join(sys.argv[1:])             # join artist name by _ if necessary
            lowerArtist = artist.lower()                # set to lower
            search = searchArtist(lowerArtist)
    else:   
        # if no arguments given just go to home page
        search = "https://rateyourmusic.com"

    webbrowser.open(search)                      # search web for artist
#----------------------------------------

def main():
    searchRym()

if __name__ == '__main__':
    main()
