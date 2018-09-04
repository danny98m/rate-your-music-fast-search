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

TODO:
    get rid of mutated variables
"""
import sys, pyperclip, webbrowser

def searchRym():
    if len(sys.argv) > 1:
        artist = '_'.join(sys.argv[1:])
        artist = artist.lower()
    else:   
        # if no arguments given just use the clipboard
        artist = pyperclip.paste()
        artist = artist.lower()
        artist = artist.split(' ')
        artist = '_'.join(artist)

    urlArtist = f'https://rateyourmusic.com/artist/{artist}'
    # here i should check url if does not exist search as film instead

    webbrowser.open(urlArtist)


def main():
    searchRym()

if __name__ == '__main__':
    main()
