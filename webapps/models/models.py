# coding= utf8
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String, Boolean, Float, CHAR, DateTime, CLOB
from sqlalchemy.orm import sessionmaker, create_session, relationships, relationship
from webapps.models.init import create_mysql_engine, get_session, Base
from datetime import date, datetime
engine = create_mysql_engine()
session = get_session(engine)

# 权限编码
KH = 0b1000     # 客户
KF = 0b0100     # 客服
JL = 0b0010     # 经理
GM = 0b0001     # 管理员

# 用户操作类别
ZC = 0b0001     # 注册
RZ = 0b0010     # 实名认证
SQ = 0b1000     # 借贷申请
SP = 0b0100     # 审批

# 资金流操作类别
HK = 0b0001     # 还款
JK = 0b0010     # 借款


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    uid = Column(CHAR(10), unique=True)
    name = Column(String(20))
    sex = Column(String(20))
    phone_number = Column(CHAR(11), unique=True)
    ID_card = Column(CHAR(18), unique=True)
    wx_id = Column(String(50), unique=True)
    email = Column(String(50), unique=True)
    credit = Column(Integer, default=0)
    # credit_data = Column(CLOB)
    ceiling = Column(Float, default=0.0)
    owed = Column(Float, default=0.0)
    address = Column(String(100), default='')

    def __str__(self):
        return '<uid={0}, phone_number={1}>'.format(self.uid, self.phone_number)

    @classmethod
    def create_new_user(cls, phone_number):
        user = User(phone_number=phone_number)
        session.add(user)
        session.commit()
        user.uid = str(user.id).rjust(10, '0')
        session.commit()
        Access.create_new_access(user.uid)
        return user

    @classmethod
    def get_user_by_phone_number(cls, phone_number):
        return session.query(cls).filter_by(phone_number=phone_number).first()

    @classmethod
    def get_user_by_uid(cls, uid):
        return session.query(cls).filter_by(uid=uid).first()


class Access(Base):
    __tablename__ = 'access'
    uid = Column(CHAR(20), ForeignKey('user.uid'), primary_key=True)
    right = Column(Integer, default=KH)
    password = Column(String(500))
    token = Column(String(24))

    def __str__(self):
        return '<uid={0} right={1}>'.format(self.uid, bin(self.right))

    @classmethod
    def create_new_access(cls, uid):
        access = cls(uid=uid)
        session.add(access)
        session.commit()
        return access

    @classmethod
    def get_right_by_uid(cls, uid):
        return session.query(cls).filter_by(uid=uid).first().right


class UserFlow(Base):
    __tablename__ = 'user_flow'
    id = Column(Integer, primary_key=True)
    start_uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=False)
    next_uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=True)
    op = Column(Integer, nullable=False, default=0)
    datetime = Column(DateTime, nullable=False)
    brief = Column(String(100))
    # extra_data = Column(CLOB)

    def __str__(self):
        return '<uid={0} op={1}>'.format(self.start_uid, bin(self.op))

    @classmethod
    def create_new_flow(cls, uid, op, extra_data, target_uid=None):
        now = datetime.now()
        brief = ""
        user_flow = UserFlow(start_uid=uid, next_uid=target_uid, op=op, datetime=now, brief=brief)
        session.add(user_flow)
        session.commit()
        return user_flow


class UserLoans(Base):
    __tablename__ = 'user_loans'
    id = Column(Integer, primary_key=True)
    uid = Column(CHAR(20), ForeignKey('user.uid'), nullable=False)
    op = Column(Integer)
    datetime = Column(DateTime)
    loads = Column(Float)
    max_loads = Column(Float)
    remain_loads = Column(Float)

    def __str__(self):
        return '<uid={0} op={1} loads={2}>'.format(self.uid, bin(self.op), str(self.loads))


def drop_all():
    Base.metadata.drop_all(engine)


def create_all():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    # drop_all()
    # create_all()
    u = User.get_user_by_phone_number('18723121650')
    print(u.id, u.uid, u.phone_number)
    aright = Access.get_right_by_uid(u.uid)
    print(aright)
    uf = UserFlow.create_new_flow(u.uid, SQ, '')
    print(uf)