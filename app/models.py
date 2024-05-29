from app.database import Base
from sqlalchemy import TIMESTAMP, Column, String, Integer, BigInteger, ForeignKey
from sqlalchemy.sql.expression import text


class Users(Base):
    __tablename__ = 'users'
    wallet_id = Column(BigInteger, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    bvn = Column(BigInteger, nullable=False)
    bvn_dob = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class UserWallet(Base):
    __tablename__ = 'user_wallets'

    id = Column(Integer, primary_key=True, nullable=False)
    wallet_name = Column(String, nullable=False)
    wallet_ref = Column(BigInteger, ForeignKey("users.wallet_id", ondelete='CASCADE'), nullable=False)
    account_number = Column(BigInteger, nullable=False)
    account_name = Column(String, nullable=False)
    bank_name = Column(String, nullable=False)
    bvn = Column(BigInteger, nullable=False)
    bvn_dob = Column(String, nullable=False)
    balance = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


