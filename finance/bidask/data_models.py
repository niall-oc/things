from sqlalchemy import Column, ForeignKey, Integer, String, create_engine,\
                       DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()
auto_increment = {'sqlite_autoincrement': True}

class Symbol(Base):
    __tablename__ = 'symbol'
    # Here we define columns for the table symbol.
    # Notice that each column is also a normal Python instance attribute.
    ticker = Column(String(8), primary_key=True, nullable=False)
    total_stocks = Column(Integer, nullable=False)

class Client(Base):
    __tablename__ = 'client'
    __table_args__ = auto_increment
    # Here we define columns for the table client.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    capital = Column(Float, nullable=False)

class Order(Base):
    __tablename__ = 'order'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    buyer_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    seller_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    quantity = Column(Integer, nullable=False)
    ask_price = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

class Owner(Base):
    __tablename__ = 'owner'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    owner_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    seller_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    quantity = Column(Integer, nullable=False)
    ask_price = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)

class Bid(Base):
    __tablename__ = 'bid'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

class Ask(Base):
    __tablename__ = 'ask'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    owner_id = Column(Integer, ForeignKey('owner.id'), nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

class Daily(Base):
    __tablename__ = 'daily'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    opening_ask = Column(Float, nullable=False)
    closing_ask = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)

class Hourly(Base):
    __tablename__ = 'hourly'
    __table_args__ = auto_increment
    id = Column(Integer, primary_key=True, nullable=False)
    ticker = Column(String(8), ForeignKey('symbol.ticker'), nullable=False)
    bid_price = Column(Float, nullable=False)
    ask_price = Column(Float, nullable=False)
    time = Column(DateTime, default=datetime.utcnow)
