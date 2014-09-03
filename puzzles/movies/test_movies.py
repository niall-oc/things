#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

class TestMovies(unittest.TestCase):
    """
    Test cases for the sorting of movie popularity by decade.
    
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
    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_find_year_for_title(self):
        """
        Given a line of input find the year of release.
        
        1. The year will always be 4 digits.
        2. The year will always succeed the movie title.
        3. If there are only 4 digits in a line of input
           AND there is no text before the 4 digits
           THEN those digits are considered part of the title.
        
        EG.
            Starwars (1977)           # year is 1997
            2001 A space odyssey 1968 # year is 1968
            2010                      # NO year
            1985.                     # NO year
            75                        # NO year
        """
        pass
