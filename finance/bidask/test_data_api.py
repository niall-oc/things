#!/usr/bin/python
# -*- coding: utf-8 -*-

"""test_data_api.py: Unit tests for data_api.py"""

__author__ = "Niall O'Connor"

import data_api
import unittest, os, random
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_models import Client, Symbol, Order, Owner, Bid, Ask, Base, Daily, Hourly

random.seed()

init_clients = (
    "**MARKET MAKER**",
    "JP Morgan and Chase",
    "Goldman Sachs",
    "Bank of America Merrill Lynch",
    "Barclays Bank Int",
    "RBS",
    "HSBC International",
    "Amercron Investments",
    "Citi Bank International",
    "Bank of Ireland",
    "Santander",
    "Bank of Tokyo",
    "Deutchebank"
    "Bank of Italy",
    "Fidelity Investments",
    "Argo Fund Management",
    "Invesco",
    "Morgan and Stanley",
    "Loyds TSB",
    "Capital One Financial",
    "Bank Of Montreal",
    "Wells Fargo",
    "Provident Financial Services",
    "BFC Financial Corp",
    "Central Pacific Financial Corp",
)

init_symbols = {
    'IBM.0001': [(5, 10.10,), (10, 10.05), (20, 10.00)],
    'MIC.0001': [(5, 5.07,),  (10, 5.05),  (20, 5.02)],
    'YHOO.001': [(5, 13.10,), (10, 13.05), (20, 13.00)]
}


class TestExcuteStockOrder(unittest.TestCase):
    """
    Test the following cases.
    
    1. Stock can be ordered from the market.
    """
    def setUp(self):
        ### Create all tables
        engine = create_engine('sqlite:///test_bid_ask_sim.db')
        Base.metadata.create_all(engine)
        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        self.session = DBSession()
        
        ### Load symbols and clients
        for ticker in init_symbols.keys():
            s = Symbol(ticker=ticker, total_stocks=1000)
            self.session.add(s)
        
        for client in init_clients:
            c = Client(name=client, capital=1000.00)
            self.session.add(c)
        
        client = self.session.query(Client).filter(Client.name == "**MARKET MAKER**").first()
        symbols = self.session.query(Symbol).all()
        price_details = {}
        
        ### Come up with quantity and prices for each order.
        for symbol in symbols:
            quantity_choices = init_symbols[symbol.ticker]
            while symbol.total_stocks > 15:
                quantity, price = random.choice(quantity_choices)
                price_details[symbol.ticker] = price_details.get(symbol.ticker, []) + [(quantity, price)]
                symbol.total_stocks -= quantity
            self.session.add(symbol)
        #print 'ORDER LOAD--------------'
        ### create and add each order
        for symbol in symbols:
            for quantity, price in price_details[symbol.ticker]:
                #print 'ORDER ', symbol.ticker
                order = Order(
                    buyer_id=client.id,
                    seller_id=client.id,
                    ticker=symbol.ticker,
                    quantity=quantity,
                    ask_price=price
                )
                self.session.add(order)
        self.session.commit()
        #print 'OWNER LOAD--------------'
        ### After speedily committing all orders
        ### execute and create owners
        orders = self.session.query(Order).all()
        for order in orders:
            #print 'OWNER ', order.ticker
            owner = Owner(
                owner_id=order.buyer_id,
                seller_id=order.seller_id,
                ticker=order.ticker,
                quantity=order.quantity,
                ask_price=order.ask_price,
                order_id=order.id
            )
            self.session.add(owner)
        self.session.commit
        
        ### Pretend this happened and update the hourly and daily stats
        for symbol in symbols:
            quantity_choices = init_symbols[symbol.ticker]
            daily = Daily(
                opening_ask=quantity_choices[-1][1],
                closing_ask=quantity_choices[-1][1],
                high=quantity_choices[-1][1],
                low=quantity_choices[-1][1],
                ticker=symbol.ticker
            )
            self.session.add(daily)
            hourly = Hourly(
                ticker=symbol.ticker,
                bid_price=quantity_choices[-1][1],
                ask_price=quantity_choices[-1][1]
            )
            self.session.add(hourly)
        self.session.commit()
    
    def tearDown(self):
        os.remove("test_bid_ask_sim.db")

    def test_place_ask(self):
        """
        An ask can be placed by a stock owner. An ask must have the following.
        
        1. The client ID. Must be in client table OR 'market' for market.
        2. A stock symbol.
        3. The quantity of stock.
        4. The ask price.
        5. A db session. Where to save the stuff!
        
        When recording an ask the time stamp is recorded.
        """
        owner = self.session.query(Owner).first()
        quantity = 10
        ask_price = 12.50
        data_api.place_ask(self.session, owner, ask_price)
        # This should be the only entry in the as table.
        a = self.session.query(Ask).first()
        self.assertTrue(a.client_id == owner.seller_id)
        self.assertTrue(a.ticker == owner.ticker)
        self.assertTrue(a.quantity == owner.quantity)
        self.assertTrue(a.price == ask_price)
        self.assertTrue(a.owner_id == owner.id)
        self.assertIsNotNone(a.time)

    def test_place_bid(self):
        """
        An bid can be placed by any client. An bid must have the following.
        
        1. The client ID. Must be in client table OR 'market' for market.
        2. A stock symbol.
        3. The quantity of stock.
        4. The ask price.
        5. A db session. Where to save the stuff!
        
        When recording an bid the time stamp is recorded.
        """
        client = self.session.query(Client).first()
        symbol = self.session.query(Symbol).first()
        quantity = 10
        price = 12.45
        data_api.place_bid(self.session, client.id, symbol.ticker, quantity, price)
        # This should be the only entry in the as table.
        b = self.session.query(Bid).first()
        self.assertTrue(b.client_id == client.id)
        self.assertTrue(b.ticker == symbol.ticker)
        self.assertTrue(b.quantity == quantity)
        self.assertTrue(b.price == price)
        self.assertTrue("%.2f"%b.price == "%.2f"%price)
        self.assertIsNotNone(b.time)

    def test_order_matching(self):
        """
        When a bid or an ask match an order can be executed.
        """
        #Grab an owner and a random client
        owner = self.session.query(Owner).first()
        client = self.session.query(Client).all()[3]
        #Create the perfect bid and ask.
        ask_price = owner.ask_price * 1.10
        data_api.place_ask(self.session, owner, ask_price)
        data_api.place_bid(self.session, client.id, owner.ticker, owner.quantity, ask_price)
        #See that the order matches the bid
        orders = data_api.match_orders(self.session, owner.ticker)
        self.assertEqual(len(orders), 1)
        order, ask = orders[0]
        self.assertEqual(order.buyer_id, client.id)
        self.assertEqual(order.seller_id, owner.owner_id)
        self.assertEqual(order.quantity, owner.quantity)
        self.assertEqual(order.ticker, owner.ticker)
        self.assertEqual(order.ask_price, owner.ask_price * 1.10)
        
    def test_execute_order(self):
        """
        An order can execute when a bid and an ask match.  When an order 
        executes the following must happen.
        
        1. The owner of the ask must be retrieved from the owners table.
        2. The stock from the owners table must be updated to the bidder.
        3. Details of the order must be added to the orders table.
        4. The bid must be removed from the bids table.
        5. The ask must be removed from the ask table.
        """
        #seed the bid and asks table
        stock_symbols = self.session.query(Symbol).all()
        print [s.ticker for s in stock_symbols]
        for symbol in stock_symbols:
            data_api.seed_bid_ask(self.session, symbol.ticker)
            matches = data_api.match_orders(self.session, symbol.ticker)
            print 'Total :', len(matches)
            if matches: # It's random after all
                data_api.execute_orders(self.session, matches)
                order_ids = [o.id for o, a in matches]
                owners_count = self.session.query(Owner).filter(Owner.order_id.in_(order_ids)).count()
                self.assertEqual(owners_count, len(matches))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestExcuteStockOrder('test_execute_order'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
