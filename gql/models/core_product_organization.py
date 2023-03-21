from sqlalchemy import Column, String, BigInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base
from .core_product import CoreProduct
from .core_organization import CoreOrganization

class CoreProductOrganization(Base):
    __tablename__ = 'core_product_organizations'
    product_id = Column(BigInteger, ForeignKey('core_products.id'), primary_key=True)
    organization_id = Column(BigInteger, ForeignKey('core_organizations.id'), primary_key=True)
    relation = Column(String(255), nullable=False)

    core_product = relationship("CoreProduct", back_populates="core_product_organizations")  # Use back_populates here
    core_organization = relationship("CoreOrganization", back_populates="core_product_organizations")
