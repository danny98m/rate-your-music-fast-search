#!/usr/bin/env python3
"""
This program takes command line arguments of a
band/artist name and goes to their rym page.

Later modify this for films and releases as well.

Unfortunately, you cannot make requests on 
rym––they will block you. So some things that could
easily be done by first making a request to check if
it returns a 404 is not possible. 

Usage: 
    Artist Search: rym.py names of artist/band seperated by spaces
    Film Search: rym.py film name of film seperated by spaces
    Album Search: rym.py album name of album seperated by spaces (THIS WILL ONLY WORK FOR FULL LENGTHS)

    Conversely if no arguments are given, artist name in clipboard will be searched.
    **Adding more search terms is not worth the effort of automating**
"""
import sys, webbrowser

def searchYear(greatYear):
    urlYear = f'https://rateyourmusic.com/charts/top/album/{greatYear}'
    return urlYear

def searchGenre(engagingGenre):
    urlGenre = f'https://rateyourmusic.com/customchart?page=1&chart_type=top&type=album&year=alltime&genre_include=1&genres={engagingGenre}&include_child_genres=t&include=both&limit=none&countries='
    return urlGenre

def searchAlbum(sickAlbum, coolArtist):
    urlAlbum = f'https://rateyourmusic.com/release/album/{coolArtist}/{sickAlbum}'
    return urlAlbum

def searchFilm(funFilm):
    urlFilm = f'https://rateyourmusic.com/film/{funFilm}'
    return urlFilm

def searchArtist(coolArtist):
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
