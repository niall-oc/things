#!/usr/bin/python
# -*- coding: utf-8 -*-

"""data_api.py: data access for bid_ask_sim.py"""

__author__ = "Niall O'Connor"

from data_models import Client, Symbol, Order, Owner, Bid, Ask

def place_ask(session, client, symbol, quantity, price):
    """
    An ask can be placed by a stock owner. An ask must have the following.
    
    :param sqlalchemy.orm.session.sessionmaker session: db session.
    :param data_models.Client client: The client asking for a bid.
    :param data_models.Symbol symbol: The Stock on offer.
    :param int quantity: The quantity being offered.
    :param float price: The price per unit of stock.
    
    This function affects state!!!
    """
    a = Ask(
        client_id=client.id,
        ticker=symbol.ticker,
        quantity=quantity,
        price=price
    ) # time is defaulted to datetime.utcnow
    session.add(a)
    session.commit()
    return True

def place_bid(session, client, symbol, quantity, price):
    """
    An bid can be placed by a client. An bid must have the following.
    
    :param sqlalchemy.orm.session.sessionmaker session: db session.
    :param data_models.Client client: The client bidding for an ask.
    :param data_models.Symbol symbol: The Stock on offer.
    :param int quantity: The quantity being offered.
    :param float price: The price per unit of stock.
    
    This function affects state!!!
    """
    b = Bid(
        client_id=client.id,
        ticker=symbol.ticker,
        quantity=quantity,
        price=price
    ) # time is defaulted to datetime.utcnow
    session.add(b)
    session.commit()
    return True
