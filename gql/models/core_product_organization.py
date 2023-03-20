from sqlalchemy import Column, String, BigInteger, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base

class CoreProductOrganization(Base):
    __tablename__ = 'core_product_organizations'
    product_id = Column(BigInteger, ForeignKey('core_products.id'), primary_key=True)
    organization_id = Column(BigInteger, ForeignKey('core_organizations.id'), primary_key=True)
    relation = Column(String(255), nullable=False)

    # Check constraint
    __table_args__ = (
        CheckConstraint(relation == 'made_by'),
    )

    core_product = relationship("CoreProduct", backref="core_product_organizations")  # Use back_populates here
    core_organization = relationship("CoreOrganization", backref="core_product_organizations")
