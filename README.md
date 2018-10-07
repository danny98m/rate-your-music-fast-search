# Rate Your Music Fast Search
This program utilizes command line arguments to quickly search the databases of rateyourmusic.com.

## Usage:
  * Artist Search: rym.py *name of artist/band seperated by spaces*
    * Brings user to entered artist's page.
    * Example: rym.py my bloody valentine  
* Film Search: rym.py **film** *name of film seperated by spaces*
  * Brings user to entered film's page.
  * Example: rym.py film eternal sunshine of the spotless mind
* Album Search: rym.py **album** *name of album seperated by spaces -- artist name seperated by spaces*
  * Brings user to entered album's page.
  * Example: rym.py album my beautiful dark twisted fantasy -- kanye west
  
* Genre Search: rym.py **genre** *name of genre seperated by spaces*
  * Brings user to top of all time list for entered genre.
  * Example: rym.py genre progressive rock
  * **Some genres require punctuation**
     * Example: rym.py genre post-punk
     
* Year Search: rym.py **year** *yearDate* (search decade by adding s at end. Example: 1990s)
  * Brings user to top of all time for given year.
  * Example: rym.py year 1977
  * You can also search by decade
     * Example: rym.py year 1980s 
     
* Top Albums of All Time: rym.py **top**
  * Brings user to overall top of all time for albums
  
* Top Films of All Time: rym.py **topfilms**
  * Brings user to overall top of all time for films
  
* RYM Home Page: rym.py
  * Brings user to rateyourmusic.com
  
* Bring Up Help Menu: rym.py **--help**

_**Album Search** will only work for full lengths. Adding every release type is more effort than automating search is worth._
