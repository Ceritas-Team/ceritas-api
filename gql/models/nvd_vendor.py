class NvdVendor(Base):
    __tablename__ = 'nvd_vendors'
    id = Column(String, primary_key=True)
    cpe_vendor = Column(String)
    date_updated = Column(DateTime)
    organization_id = Column(String, ForeignKey('core_organizations.id'))
    nvd_products = relationship("NvdProduct", back_populates="nvd_vendors")
    core_organizations = relationship("CoreOrganization", back_populates="nvd_vendors")