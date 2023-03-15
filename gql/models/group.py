from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
# from .instance_group import InstanceGroup
from .product_instance_group import ProductInstanceGroup
class Group(Base):
    __tablename__ = 'groups'
    id = Column(String, primary_key=True)
    product_instance_groups = relationship("ProductInstanceGroup", back_populates="groups")
    # product_instance_groups = relationship("ProductInstanceGroup", back_populates="groups")
    # instance_group = relationship("InstanceGroup", back_populates="groups")
    name = Column(String)
    company_id = Column(String, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="groups")
    created_by = Column(String)
    is_default = Column(Boolean)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    deleted_at = Column(DateTime)