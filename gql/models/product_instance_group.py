from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
# from .group import Group
from .product_instance import ProductInstance
class ProductInstanceGroup(Base):
    __tablename__ = 'product_instance_group'
    id = Column(String, primary_key=True)
    
    group_id = Column(String, ForeignKey('groups.id'))
    
    groups = relationship("Group", back_populates="product_instance_groups")
    product_instances = relationship("ProductInstance", back_populates="product_instance_group")
    product_instance_id = Column(String, ForeignKey('product_instance_group.id'))
    # product_instance_id= Column(String, ForeignKey('product_instances.id'))