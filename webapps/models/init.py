# coding= utf8
# coding= utf8
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean, Float, CHAR
from sqlalchemy.orm import sessionmaker, create_session, relationships, relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def create_sqlite_session(echo=False):
    conn_str = 'sqlite:///test.db'
    engine = create_engine(conn_str, echo=echo)
    db_session = sessionmaker(bind=engine)
    return db_session()
