from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from . import Base
from sqlalchemy.orm import relationship
class ProductInstance(Base):
    __tablename__ = 'product_instances'
    id = Column(String, primary_key=True)
    product_id = Column(String, ForeignKey('product_instance_group.id'))
    
    # parent_instance_id = Column(String)
    date_added = Column(DateTime)
    core_product_id = Column(String, ForeignKey('core_products.id'))
    core_products = relationship("CoreProduct", back_populates="product_instances")
    # product_instance_mitigations = relationship("ProductInstanceMitigation", back_populates="product_instances")
    product_instance_group = relationship("ProductInstanceGroup", back_populates="product_instances")
