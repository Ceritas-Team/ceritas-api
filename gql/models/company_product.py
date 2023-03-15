from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
from .core_product import CoreProduct
from .instance import Instance
class CompanyProduct(Base):
    __tablename__ = 'company_product'
    id = Column(String, primary_key=True)
    company_id = Column(String, ForeignKey('companies.id'))
    core_product_id = Column(String, ForeignKey('core_products.id'))
    date_added = Column(DateTime)
    instances = relationship("Instance", back_populates="company_product")
    company = relationship("Company", back_populates="company_product")
    core_products = relationship("CoreProduct", back_populates="company_product")