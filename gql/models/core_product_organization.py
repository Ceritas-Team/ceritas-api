class CoreProductOrganization(Base):
    __tablename__ = 'core_product_organizations'
    product_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
    organization_id = Column(String, ForeignKey('core_organizations.id'), primary_key=True)
    core_organizations = relationship("CoreOrganization", back_populates="core_product_organizations")
    relationship = Enum('relationship', 'made_by', name='relationship')
    core_products = relationship("CoreProduct", back_populates="core_product_organizations")