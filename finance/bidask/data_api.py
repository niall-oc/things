#!/usr/bin/python
# -*- coding: utf-8 -*-

"""data_api.py: data access for bid_ask_sim.py"""

__author__ = "Niall O'Connor"

from data_models import Client, Symbol, Order, Owner, Bid, Ask

def place_ask(session, owner, ask_price):
    """
    An ask can be placed by a stock owner. An ask must have the following.
    
    :param sqlalchemy.orm.session.sessionmaker session: db session.
    :param int owner: The seller asking for a bid.
    :param float ask_price: The price per unit of stock.
    
    This function affects state!!!
    """
    a = Ask(
        client_id=owner.owner_id,
        ticker=owner.ticker,
        quantity=owner.quantity,
        price=ask_price,
        owner_id=owner.id
    ) # time is defaulted to datetime.utcnow
    session.add(a)
    session.commit()
    return True

def place_bid(session, client_id, ticker, quantity, price):
    """
    An bid can be placed by a client. An bid must have the following.
    
    :param sqlalchemy.orm.session.sessionmaker session: db session.
    :param int client_id: The client bidding for an ask.
    :param str ticker: The Stock on offer.
    :param int quantity: The quantity being offered.
    :param float price: The price per unit of stock.
    
    This function affects state!!!
    """
    b = Bid(
        client_id=client_id,
        ticker=ticker,
        quantity=quantity,
        price=price
    ) # time is defaulted to datetime.utcnow
    session.add(b)
    session.commit()
    return True

def _sorted_bids(session, ticker, quantity):
    bids = session.query(Bid).filter(Bid.ticker == ticker).filter(Bid.quantity == quantity).all()
    return sorted(bids, key=lambda x: x.price, reverse=True)
            
def _sorted_asks(session, ticker):
    asks = session.query(Ask).filter(Ask.ticker == ticker).all()
    return sorted(asks, key=lambda x: x.price, reverse=True)

def match_orders(session, ticker):
    """
    Scan the asks and bids table and find matches. The algorithm is as follows.
    
    1. Group all bids from lowest to highest.
    2. Group all asks from lowest to highest.
    3. For a ticker find the lowest ask price.
    4. For the same ticker check each bid until you find one equal or greater
       than the ask price
    
    This always ensures the bid >= ask.
    :param str ticker: The stock ticker we want to match orders on.
    """
    orders = []
    for ask in _sorted_asks(session, ticker): # queried once
        for bid in _sorted_bids(session, ticker, ask.quantity): # queried many
            if bid < ask:
                continue
            else:# bid >= ask, meaning this ask can be filled first
                order = Order(
                    buyer_id=bid.client_id,
                    seller_id=ask.client_id,
                    ticker=ask.ticker,
                    quantity=ask.quantity,
                    ask_price=ask.price
                )
                orders.append(order)
                break
        # important to remove a bid once it has become an order
        session.delete(bid)
        session.commit()
    return orders

