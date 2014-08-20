einstein
========

This is a famous puzzle first proposed by Albert Einstein.  He proposed the 98% of the world cannot work this out.  I first came across this when I was 22.  It took me 4 days to figure it out very inefficently.  The ends justified the means :-)

Recently I was curious about using a test driven approach to solving the problem.  My theory was that a machine given the rules could show you the best solution.  I've always believed Albert Einstein was a brilliant man who could visualise a simple model to represent a complex thing.  After this exercise I believe he also had a sneaky sense of humor and that there may be a lot between the lines we have missed.

Who owns the fish?
==================

This is the question at the heart of this problem.  We are given 15 rules which describe the fixed state of a system.  From these 15 rules we are asked who owns the fish.

The system consists of 5 houses in a row.  Each house has the following properties { house_color, nationality, drink, pet, spport }.  For example the first house in the row could have the following properties.

```{
    'house_color': 'green',
    'nationality': 'irish', # obviously :-)
    'drink'      : 'water', # shame if you are surprised :-)
    'pet'        : 'horse',
    'sport'      : 'hurling' # look it up
}```

For each of the 5 houses you must choose from the folling options.  Cigarette's were used when I first encountered this BUT they're plain wrong.

| Property    | Posibilities |
-----------------------------|
| nationality | norweigan, german, danish, british, swedish |
| house_color | red, green, yellow, blue, white |
| drink | water, tea, coffee, beer, milk |
| pet | dog, cat. horse, bird, fish |
| sport | billiards, polo, soccer, hockey, polo |

The rules ( state of the world )
================================

1. The Brit lives in a red house
2. The Swede keeps dogs
3. The Dane drinks tea
4. The green house is on the left of the white house
5. The green house owner drinks coffee
6. The person who plays polo rears birds
7. The owner of the yellow house plays hockey
8. The man living in the house right in the center drinks milk
9. The Norwegian lives in the first house
10. The man who plays baseball lives next to the man who keeps cats
11. The man who keeps horses lives next to the one who plays hockey
12. The man who plays billiards drinks beer
13. The German plays soccer
14. The Norwegian lives next to the blue house
15. The man who plays baseball has a neighbor who drinks water.

The goal
========

Fill in the blanks.

|| House1 | House2 | House3 | House4 | House5 |
-----------------------------------------------
|house_color||||||
|nationality||||||
|drink||||||
|pet||||||
|drink||||||
