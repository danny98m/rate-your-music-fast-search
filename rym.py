#! /usr/bin/env python3
"""
This program takes a command line arguments of a
band/artist name and goes to their rym page.

Later modify this for films and releases as well.
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

	url = f'https://rateyourmusic.com/artist/{artist}'

	webbrowser.open(url)


def main():
	searchRym()

if __name__ == '__main__':
	main()
