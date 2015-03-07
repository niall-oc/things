#!/usr/bin/python
# -*- coding: utf-8 -*-

"""monte_carlo.py: simulation for bid_ask_sim.py"""

__author__ = "Niall O'Connor"

import random

random.seed()

flip = lambda : random.choice([-1, 1])
dice = lambda : random.randint(1, 6)

def trend(path):
    result = [0] # we need a starting point
    for p in path:
        result.append(result[-1] + p)
    return result

path = lambda x: [flip() * dice() for n in range(x)]
