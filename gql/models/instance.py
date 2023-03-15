from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
# from .company_product import CompanyProduct
from .instance_group import InstanceGroup
class Instance(Base):
    __tablename__ = 'instances'
    id = Column(String, primary_key=True)
    company_product_id = Column(String, ForeignKey('company_product.id'))
    location_id = Column(String, ForeignKey('company_location.id'))
    company_asset_id = Column(String)
    date_added = Column(DateTime)
    company_product = relationship("CompanyProduct", back_populates="instances")
    # company_location = relationship("CompanyLocation", back_populates="instances")
    instance_group = relationship("InstanceGroup", back_populates="instances")
    # instance_mitigations = relationship("InstanceMitigation", back_populates="instances")