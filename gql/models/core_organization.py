class CoreOrganization(Base):
    __tablename__ = 'core_organizations'
    id = Column(String, primary_key=True)
    uuid = Column(String)
    name = Column(String)
    img_link = Column(String)
    jsondata = Column(String)
    core_product_organizations = relationship("CoreProductOrganization", back_populates="core_organizations")
    core_rating_history = relationship("CoreRatingHistory", back_populates="core_organizations")
    core_risks_history = relationship("CoreRisksHistory", back_populates="core_organizations")
    nvd_vendors = relationship("NvdVendor", back_populates="core_organizations")