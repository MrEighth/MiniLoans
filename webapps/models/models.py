# coding= utf8
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean, Float, CHAR, DateTime, CLOB
from sqlalchemy.orm import sessionmaker, create_session, relationships, relationship
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from webapps.models.init import create_sqlite_session
Base = declarative_base()
session = create_sqlite_session()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uid = Column(CHAR(20), unique=True)
    name = Column(String(20))
    sex = Column(String(20))
    phone_number = Column(CHAR(11), unique=True)
    ID_card = Column(CHAR(18), unique=True)
    wx_id = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    credit = Column(Integer)
    credit_data = Column(CLOB)
    ceiling = Column(Float)
    owed = Column(Float)
    address = Column(String(100))

    @classmethod
    def add_new_user(cls, phone_number):
        user = User(phone_number=phone_number)
        session.add(user)
        session.commit()
        return user

    @classmethod
    def get_user_by_phone_number(cls, phone_number):
        return session.query(cls).filter_by(phone_number=phone_number).first()


class Access(Base):
    KH = 0b1000
    KF = 0b0100
    JL = 0b0010
    GM = 0b0001

    __tablename__ = 'access'
    uid = Column(CHAR(20), ForeignKey('user.uid'), primary_key=True)
    right = Column(Integer, default=KH)
    password = Column(String(500))
    token = Column(String(24))


class UserFlow(Base):
    ZC = 0b0001
    RZ = 0b0010
    SQ = 0b1000
    SP = 0b0100

    __tablename__ = 'user_flow'
    id = Column(Integer, primary_key=True)
    start_uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=False)
    next_uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=True)
    op = Column(Integer, nullable=False, default=0)
    datetime = Column(DateTime, nullable=False)
    brief = Column(String(100))


class UserLoads(Base):
    HK = 0b0001
    JK = 0b0010

    __tablename__ = 'user_loads'
    id = Column(Integer, primary_key=True)
    uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=False)
    op = Column(Integer)
    datetime = Column(DateTime)
    loads = Column(Float)
    max_loads = Column(Float)
    remain_loads = Column(Float)


def init():
    engine = create_engine('sqlite:///test.db')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    User.add_new_user('18723121647')


if __name__ == '__main__':
    init()
    u = User.get_user_by_phone_number('18723121647')
    print(u, u.id, u.phone_number)