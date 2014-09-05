#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Given the following list in a string seperated by \n characters.
    Jaws (1975)
    Starwars 1977
    2001 A Space Odyssey ( 1968 )
    Back to the future 1985.
    Raiders of the lost ark 1981 .
    jurassic park 1993
    The Matrix 1999
    A fist full of Dollars
    10,000 BC (2008)
    1941 (1979)
    24 Hour Party People (2002)
    300 (2007)
    2010

Produce the following output.
    2000s : 3
    1970s : 3
    1980s : 2
    1990s : 2
    1960s : 1
"""
import re

year_pattern = re.compile("\d{4}") # or [0-9]{4}

def find_year(title):
    """
    Returns a 4 digit block nearest the right of the string title.
    OR
    Returns None.
    
    EG.
    Starwars (1977)           # year is 1997
    2001 A space odyssey 1968 # year is 1968
    2010                      # NO year
    1985.                     # NO year
    75                        # NO year
    
    usage:
       >>> find_year("starwars (1977)")
       1977
    
    :param str title: A string containing a movie title and year of relaease.
    :return str: Year of release
    """
    # find all patterns that match the year pattern
    matches = year_pattern.findall(title)
    # if any matches
    if matches:
        # record for convienence
        year = matches[-1]
        too_short = len(title) < 8
        # If the year is the title then return None
        if year == title:
            return None
        # If we have enough room for 1 block of 4 digits and its at the start
        elif too_short and title.startswith(year):
            return None
        else:
            return year

def rank_decades(movies):
    """
    Returns a dictionary of decades -> number of movies released.
    
    usage:
        >>> rank_decades(['starwars 1977'])
        {'1970s': 1}
    
    :param list movies: A collection of title strings
    :return dict: decades and number of releases.
    """
    results = {}
    for movie in movies:
        year = find_year(movie)
        # If we found a release year then count it
        if year: 
            # A way to map year to decade
            decade = "{0}0s".format(year[:3])
            results[decade] = results.setdefault(decade, 0) + 1
    return results

if __name__ == "__main__":
    f = open('movie_releases.txt')
    movie_data = f.read()
    all_movies = movie_data.split('\n')
    rank = rank_decades(all_movies)
    for decade, count in sorted(rank.items(), key=lambda s: s[1], reverse=True):
        print "%s : %s" % (decade, count,)
