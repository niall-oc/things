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

