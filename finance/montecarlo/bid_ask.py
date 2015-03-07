#!/usr/bin/python
# -*- coding: utf-8 -*-

"""bid_ask.py: simulation for market bid asks"""

__author__ = "Niall O'Connor"

import monte_carlo
import random
from matplotlib import pyplot
random.seed()

def generate_prices(reference_price, sigma, total):
    """
    Generate a total number of bids using a normal variate with a deviation no
    greater than sigma.
    """
    return [random.normalvariate(reference_price, sigma) for i in range(total)]

if __name__ == '__main__':
    time_steps = 100
    num_paths = 1
    ticker = 'TWTR.001'
    ask_price = 44.23
    
    ### tweaks
    bid_follow = .98
    shock = 0.0
    num_asks = 30
    num_bids = 30
    sigma = .01
    
    for i in range(num_paths):
        path = monte_carlo.path(time_steps)
        print path
        
        reference_price = ask_price + shock
        max_ask = []
        for time_step in path:
            ask_mu = reference_price+time_step
            bid_mu = (reference_price+time_step) * bid_follow
            asks = generate_prices(ask_mu, sigma, num_asks)
            bids = generate_prices(bid_mu, sigma, num_bids)
            #print 'BIDS--\n%s\n\n' % bids
            #print 'ASKS--\n%s\n\n' % asks
            ask_price = max(asks)
            max_ask.append(ask_price)
        pyplot.plot(max_ask)
            
    pyplot.show()
