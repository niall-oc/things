#!/usr/bin/python
# -*- coding: utf-8 -*-

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
