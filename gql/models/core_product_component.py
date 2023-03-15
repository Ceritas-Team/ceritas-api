from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class CoreProductComponent(Base):
    __tablename__ = 'core_product_component'
    parent_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
    child_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
    child = relationship("CoreProduct", foreign_keys=[child_id], back_populates="core_product_component")
    parent = relationship("CoreProduct", foreign_keys=[parent_id], back_populates="core_product_component")