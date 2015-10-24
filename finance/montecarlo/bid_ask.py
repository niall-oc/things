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

def match_orders(bids, asks):
    """
    Given a list of bids and a list of asks. Find all matches
        
        logic.
        
        1. Find the lowest Ask.
        2. Find the first bid that is >= to this ask.
        3. Remove the bid and ask from each list.
        4. When the highest bid is lower than the lowest ask we have a spread.
        5. When complete return the matched orders, remaining asks and remaining bids.
    """
    matches = []; remove_bids = []; remove_asks = []
    spread_not_found = True
    
    while spread_not_found:
        # find match and reset bids and asks.
        
        for ask in sorted(asks):
            for bid in sorted(bids):
                if bid >= ask:
                    # order can match.
                    matches.append((bid, ask,))
                    break
            bids.remove(bid)
            asks.remove(ask)
            break
        if max(bids) < min(asks):
            spread_not_found = False
    results = {'matches': matches, 'remaining_bids': bids, 'remaining_asks': asks}
    return results
                

if __name__ == '__main__':
    # constants for this simulation
    time_steps = 24
    num_paths = 1
    ticker = 'TWTR.001'
    ask_price = 44.23
    
    ### tweaks
    bid_follow = .992
    shock = 0.0
    num_asks = 100
    num_bids = 100
    sigma = .5
    
    for i in range(num_paths):
        path = monte_carlo.path(time_steps)
        print path
        
        reference_price = ask_price + shock
        ask_trend = []
        bid_trend = []
        matches = [0]
        for time_step in path:
            ask_mu = reference_price+time_step
            bid_mu = (reference_price+time_step) * bid_follow
            asks = generate_prices(ask_mu, sigma, num_asks)
            bids = generate_prices(bid_mu, sigma, num_bids)
            results = match_orders(bids, asks)
            ask_trend.append(min(results['remaining_asks']))
            bid_trend.append(max(results['remaining_bids']))
            matches.append(matches[-1] + len(results['matches']))
            
        #plot the stock movement.
        #pyplot.plot(ask_trend)
        #pyplot.plot(bid_trend)
        pyplot.plot(matches)
        # plot the over all slope
            
    pyplot.show()
