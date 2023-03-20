from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, JSON, BigInteger
from . import Base
from sqlalchemy.orm import relationship
from .core_product_component import CoreProductComponent

class CoreProduct(Base):
    __tablename__='core_products'
    id = Column(BigInteger, primary_key=True)
    uuid = Column(String)
    type = Enum('product', 'component', name='type')
    category = Column(String)
    img_link = Column(String)
    jsondata = Column(JSON)
    name = Column(String)
    label_id = Column(BigInteger, ForeignKey('core_labels.id'))
    hbom = Column(JSON)
    current_rating_history_id = Column(BigInteger, ForeignKey('core_rating_history.id'))
    # core_rating_history = relationship("CoreRatingHistory", back_populates="core_products")
    # product_instances = relationship("ProductInstance", back_populates="core_products")
    # core_product_organizations = relationship("CoreProductOrganization", back_populates="core_products")
    # vulnerability_core_product = relationship("VulnerabilityCoreProduct", back_populates="core_products")
    # nvd_products = relationship("NvdProduct", back_populates="core_products")
    product_instances = relationship("ProductInstance", back_populates="core_products")
    # nvd_linked = relationship("NvdLink", back_populates="core_products")
    core_product_component = relationship("CoreProductComponent", foreign_keys=[CoreProductComponent.parent_id], back_populates="parent")
    #current_rating_history = relationship("CoreRatingHistory", foreign_keys=[current_rating_history_id], backref="core_products")
    # company_product = relationship("CompanyProduct", back_populates="core_products")
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "type": self.type,
    #         "name": self.name,
    #         # Add all other fields of the CoreProduct model here
    #     }
    core_labels = relationship("CoreLabel", foreign_keys=[label_id], backref="core_products")