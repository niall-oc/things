#!/usr/bin/python
# -*- coding: utf-8 -*-

"""test_bid_ask.py: simulation for bid_ask.py"""

__author__ = "Niall O'Connor"

import unittest
import bid_ask

class TestBidAsk(unittest.TestCase):
    """
    Test the bid and ask generators.
    Test order matching.
    Test spread determination.
    """
    def test_bids(self):
        """
        Given a reference price use a random function to seed a number of prices.
        """
        reference_price = 10.12
        sigma = .1
        total = 50
        bids = bid_ask.generate_prices(reference_price, sigma, total)
        self.assertEqual(len(bids), total)
    
    def test_order_matching(self):
        """
        Given a list of bids and a list of asks. Find all matches
        
        logic.
        
        1. Find the lowest Ask.
        2. Find the first bid that is >= to this ask.
        3. Remove the bid and ask from each list.
        4. When complete return the matched orders, remaining asks and remaining bids.
        """
        # Inputs are bids and asks, expect output is matches and remainders.
        test_harness = (
            (   # inputs
                {
                    'bids': [10.01, 10.02, 10.04, 10.05, 10.06],
                    'asks': [10.04, 10.05, 10.07, 10.09, 10.10]
                },
                # expected outputs
                {
                    'matches': [(10.04, 10.04,), (10.05, 10.05,)],
                    'remaining_bids': [10.01, 10.02, 10.06],
                    'remaining_asks': [10.07, 10.09, 10.10]
                },
            ),            
        )
        for given, expect in test_harness:
            outputs = bid_ask.match_orders(given['bids'], given['asks'])
            self.assertEqual(expect['remaining_bids'], outputs['remaining_bids'])
            self.assertEqual(expect['remaining_asks'], outputs['remaining_asks'])
            self.assertEqual(expect['matches'], outputs['matches'])

