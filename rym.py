#! /usr/bin/env python3
"""
This program takes a command line arguments of a
band/artist name and goes to their rym page.

Later modify this for films and releases as well.

Unfortunately, you cannot make requests on 
rym––they will block you. So some things that could
easily be done by first making a request to check if
it returns a 404 is not possible. 

Look in to urllib instead.

Usage: 
    Artist Search: rym.py names of artist/band seperated by spaces
    Film Search: rym.py film name of film seperated by spaces //NOT YET IMPLEMENTED

    Conversely if no arguments are given, artist name in clipboard will be searched.

TODO:
"""
import sys, pyperclip, webbrowser

def searchRym():
    if len(sys.argv) > 1:
        artist = '_'.join(sys.argv[1:])             # join artist name by _ if necessary
        lowerArtist = artist.lower()                # set to lower
    else:   
        # if no arguments given just use the clipboard
        artist = pyperclip.paste()                  # paste from clipboard
        splitArtist = artist.split()                # split artist by whitespace
        joinedArtist = '_'.join(splitArtist)        # join by _ if necessary 
        lowerArtist = joinedArtist.lower()          # set to lower

    urlArtist = f'https://rateyourmusic.com/artist/{lowerArtist}'
    # here i should check url if does not exist search as film instead

    webbrowser.open(urlArtist)


def main():
    searchRym()

if __name__ == '__main__':
    main()
