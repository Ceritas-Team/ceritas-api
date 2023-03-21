from sqlalchemy import Column, String, DateTime, BigInteger
from sqlalchemy.orm import relationship
from . import Base
from .group import Group
class Company(Base):
    __tablename__ = 'companies'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    description = Column(String)
    website = Column(String)
    address_1 = Column(String)
    address_2 = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)
    country = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    # company_product = relationship("CompanyProduct", back_populates="company")
    # company_location = relationship("CompanyLocation", back_populates="company")
    groups = relationship("Group", back_populates="company")