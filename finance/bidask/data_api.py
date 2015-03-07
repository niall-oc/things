#!/usr/bin/python
# -*- coding: utf-8 -*-

"""data_api.py: data access for bid_ask_sim.py"""

__author__ = "Niall O'Connor"

from data_models import Client, Symbol, Order, Owner, Bid, Ask, Daily, Hourly
import random
import monte_carlo

random.seed()

flip = lambda : random.choice([-1, 1])
dice = lambda : random.random()/5

def skew_price(price):
    if flip() > 0:
        mu_price = price + dice()
    else:
        mu_price = price - dice()
    return mu_price

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
    return session.query(Bid).filter(Bid.ticker == ticker).order_by(Bid.price.desc()).all()
            
def _sorted_asks(session, ticker):
    return session.query(Ask).filter(Ask.ticker == ticker).order_by(Ask.price.desc()).all()

def match_orders(session, ticker):
    """
    Scan the asks and bids table and find matches. The algorithm is as follows.
    
    1. Group all bids from lowest to highest.
    2. Group all asks from lowest to highest.
    3. For a ticker find the lowest ask price.
    4. For the same ticker check each bid until you find one equal or greater
       than the ask price
    
    This always ensures the bid >= ask.  Bids are removed and converted to orders.
    :param str ticker: The stock ticker we want to match orders on.
    """
    #print "MATCH ORDERS CALLED : ", ticker
    orders = []
    for ask in _sorted_asks(session, ticker): # queried once
        for bid in _sorted_bids(session, ticker, ask.quantity): # queried many
            #print ticker, "%2.6f"%bid.price, "%2.6f"%ask.price, "%2i"%bid.quantity, "%2i"%ask.quantity
            if bid.price < ask.price:
                continue
            else:# bid >= ask, meaning this ask can be filled first
                #print 'SALE-', ticker, "%2.6f"%bid.price, "%2.6f"%ask.price
                order = Order(
                    buyer_id=bid.client_id,
                    seller_id=ask.client_id,
                    ticker=ask.ticker,
                    quantity=ask.quantity,
                    ask_price=ask.price
                )
                session.add(order)
                orders.append((order, ask,))
                session.delete(bid)
                break
        # important to remove a bid once it has become an order
        session.commit()
    return orders

def execute_orders(session, matches):
    """
    On order stems from an accepted bid.  A bid is essentially removed and an
    order created.  When an order is executed the stock gets a new owner.
    When the stock has a new owner the ask that was matched to the bid must then
    also be removed.
    """
    for order, ask in matches:
        owner = session.query(Owner).filter(Owner.id == ask.owner_id).one()
        owner.seller_id = order.seller_id
        owner.owner_id = order.buyer_id
        owner.ask_price = order.ask_price
        owner.ticker = order.ticker
        owner.quantity = order.quantity
        owner.order_id = order.id
        session.add(owner)
        session.delete(ask)
    session.commit()

def _seed_bids(session, ticker, price):
    """
    Traverse all clients and create a bid for this ticker.
    The bid price will be .1 standard deveation point.
    """
    clients = session.query(Client).all()
    bids = []
    for i in range(30):
        client = random.choice(clients)
        #print client.name
        quantity = 10
        bid_price = random.normalvariate(price, .04)
        bids.append(
            Bid(
                client_id=client.id,
                ticker=ticker,
                quantity=quantity,
                price=bid_price
            )
        )
    return bids

def _seed_asks(session, ticker, price):
    """
    Traverse all owners to generate asks.
    The ask price will be .1 standard deveation point.
    """
    owners = session.query(Owner).filter(Owner.ticker == ticker).all()
    asks = []
    for i in range(int(len(owners)/3)):
        owner = owners[i]
        ask_price = random.normalvariate(price, .04)
        asks.append(
            Ask(
                client_id=owner.owner_id,
                ticker=owner.ticker,
                quantity=owner.quantity,
                price=ask_price,
                owner_id=owner.id
            )
        )

    return asks

def seed_bid_ask(session, ticker):
    """
    Create random bids and asks.
    """
    #print 'SEED BID ASK - ', ticker
    hourly = session.query(Hourly).filter(Hourly.ticker == ticker).order_by(Hourly.time.desc()).first()
    # montecarlo movement shifts the market
    mu_ask_price = skew_price(hourly.ask_price)
    mu_bid_price = hourly.bid_price - dice()
    # bid price always trails ask
    bids = _seed_bids(session, ticker, mu_bid_price)
    asks = _seed_asks(session, ticker, mu_ask_price)
    #print len(bids), len(asks)
    for bid in bids:
        session.add(bid)
    for ask in asks:
        session.add(ask)
    session.commit()

def dump_bid_ask(session, ticker):
    print '----------------------'
    bids = session.query(Bid).filter(Bid.ticker == ticker).order_by(Bid.price.desc()).all()
    for b in bids:
        print 'BIDS - ', b.ticker, "%2i"%b.quantity, "%2.6f"%b.price
    # the lowest ask for a ticker
    print '----------------------'
    asks = session.query(Ask).filter(Ask.ticker == ticker).order_by(Ask.price.asc()).all()
    for a in asks:
        print 'ASKS - ', a.ticker, "%2i"%a.quantity, "%2.6f"%a.price

def hourly_stats(session, ticker):
    """
    """
    # the highest bid for a ticker
    bid = session.query(Bid).filter(Bid.ticker == ticker).order_by(Bid.price.desc()).first()
    # the lowest ask for a ticker
    ask = session.query(Ask).filter(Ask.ticker == ticker).order_by(Ask.price.asc()).first()
    hourly = Hourly(
        ticker=ticker,
        bid_price=bid.price,
        ask_price=ask.price
    )
    session.add(hourly)
    session.commit()
    
