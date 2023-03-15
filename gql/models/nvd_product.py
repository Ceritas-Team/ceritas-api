class NvdProduct(Base):
    __tablename__ = 'nvd_products'
    id = Column(String, primary_key=True)
    cpe_short_product = Column(String)
    cpe_product_name = Column(String)
    date_updated = Column(DateTime)
    date_link = Column(DateTime)
    core_product_id = Column(String, ForeignKey('core_products.id'))
    nvd_vendor_id = Column(String, ForeignKey('nvd_vendors.id'))
    nvd_vendors = relationship("NvdVendor", back_populates="nvd_products") 
    nvd_cpe_matches = relationship("NvdCpeMatch", back_populates="nvd_products")
    core_products = relationship("CoreProduct", back_populates="nvd_products")