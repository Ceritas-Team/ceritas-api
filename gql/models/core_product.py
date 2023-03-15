from sqlalchemy import Column, String, DateTime, ForeignKey, Enum
from . import Base
from sqlalchemy.orm import relationship
from .core_product_component import CoreProductComponent
class CoreProduct(Base):
    __tablename__='core_products'
    id = Column(String, primary_key=True)
    type = Enum('product', 'component', name='type')
    category = Enum('IT', 'OT', name='category')
    img_link = Column(String)
    jsondata = Column(String)
    name = Column(String)
    label_id = Column(String, ForeignKey('core_labels.id'))
    # core_labels = relationship("CoreLabel", back_populates="core_products")
    # current_rating_history_id = Column(String, ForeignKey('core_rating_history.id'))
    # core_rating_history = relationship("CoreRatingHistory", back_populates="core_products")
    # product_instances = relationship("ProductInstance", back_populates="core_products")
    # core_product_organizations = relationship("CoreProductOrganization", back_populates="core_products")
    # vulnerability_core_product = relationship("VulnerabilityCoreProduct", back_populates="core_products")
    # nvd_products = relationship("NvdProduct", back_populates="core_products")
    product_instances = relationship("ProductInstance", back_populates="core_products")
    # nvd_linked = relationship("NvdLink", back_populates="core_products")
    core_product_component = relationship("CoreProductComponent", foreign_keys=[CoreProductComponent.parent_id], back_populates="parent")
    # core_rating_history = relationship("CoreRatingHistory", back_populates="core_products")
    # company_product = relationship("CompanyProduct", back_populates="core_products")
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "type": self.type,
    #         "name": self.name,
    #         # Add all other fields of the CoreProduct model here
    #     }