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
    matches = year_pattern.findall(title)
    if matches:
        return matches[-1]
    

