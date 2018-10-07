#!/usr/bin/env python3
"""
This program takes command line arguments of a
band/artist name and goes to their rym page.

Later modify this for films and releases as well.

Unfortunately, you cannot make requests on 
rym––they will block you. So some things that could
easily be done by first making a request to check if
it returns a 404 is not possible. 


Input Info:
    Write & as and 
    Don't include apostrophes or accent marks
    Seperate hypenated words: wu-tang clan entered as wu tang clan
Usage: 
    Artist Search: rym.py names of artist/band seperated by spaces
    Film Search: rym.py film name of film seperated by spaces
    Album Search: rym.py album name of album seperated by spaces (THIS WILL ONLY WORK FOR FULL LENGTHS)
    Genre Search: rym.py genre name of genre seperated by spaces
    Year Search: rym.py year yearDate (search by decade by adding s at end. Example: 1990s)

    **Adding more search terms is not worth the effort of automating**

    TODO:
    check for artists and albums as well
    Add top films
    ADD help command
    Make album search not require input can look for --- or something to seperate
    Make punct list into tuple
"""
import sys, webbrowser

# Removes certain characters from input that rym doesn't like
def checkValid(userInput):
    problemPunctuations = [':', ',', '.', '!']
    for puncType, punct in enumerate(problemPunctuations):
        while problemPunctuations[puncType] in userInput:
            problemCharIndex = userInput.index(punct)
            if puncType == '!' or puncType == '?':
                userInput = userInput[:problemCharIndex] + userInput[problemCharIndex+1:]
            else:
                userInput = userInput[:problemCharIndex] + "_" + userInput[problemCharIndex+1:]
    return userInput


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

def searchRym():
    if len(sys.argv) > 1:
        # Search by film
        if (sys.argv[1] == "film"):
            film = '_'.join(sys.argv[2:])
            lowerFilm = film.lower()
            search = searchFilm(lowerFilm)
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
            album = '_'.join(sys.argv[2:])
            lowerAlbum = album.lower()
            artist = input("Enter Artist Name: ")
            splitArtist = artist.split()
            joinedArtist = '_'.join(splitArtist)
            lowerArtist = joinedArtist.lower()
            search = searchAlbum(lowerAlbum, lowerArtist)
        # Top of all time
        elif (sys.argv[1] == "top"):
            search = "https://rateyourmusic.com/customchart"
        else:
            artist = '_'.join(sys.argv[1:])             # join artist name by _ if necessary
            lowerArtist = artist.lower()                # set to lower
            search = searchArtist(lowerArtist)
    else:   
        # if no arguments given just go to home page
        search = "https://rateyourmusic.com"

    webbrowser.open(search)                      # search web for artist

def main():
    searchRym()

if __name__ == '__main__':
    main()
