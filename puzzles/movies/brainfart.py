#!/usr/bin/python
# -*- coding: utf-8 -*-

movies = """Jaws (1975)
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
2010"""

get_year = lambda m : ''.join([n for n in m if n.isdigit()])[-4:]

results = dict()
for movie in movies:
    year = get_year(movie)
    if year:
        decade = "{0}0s".format(year[:3])
        results[decade] = results.setdefault(decade, 0) + 1

output = sorted(results.items(), key=lambda m: m[1], reverse=True)
for year, n in output:
   print "{0} : {1}".format(year, n)

