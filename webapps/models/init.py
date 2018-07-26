# coding= utf8
# coding= utf8
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean, Float, CHAR
from sqlalchemy.orm import sessionmaker, create_session, relationships, relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


def create_sqlite_engine(db='test.db', echo=False):
    conn_str = 'sqlite:///{0}'.format(db)
    engine = create_engine(conn_str, echo=echo)
    return engine


def create_mysql_engine(uid='root', pwd='password', host='localhost', port='3306', db='test', echo=False):
    conn_str = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(uid, pwd, host, port, db)
    engine = create_engine(conn_str, echo=echo)
    return engine


def get_session(engine):
    db_session = sessionmaker(bind=engine)
    return db_session()


if __name__ == '__main__':
    engine = create_sqlite_engine()
    session = get_session(engine)