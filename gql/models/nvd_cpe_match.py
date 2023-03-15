class NvdCpeMatch(Base):
    __tablename__ = 'nvd_cpe_matches'
    id = Column(String, primary_key=True)
    cpe = Column(String)
    date_upated = Column(DateTime)
    version_json = Column(String)
    nvd_product_id = Column(String, ForeignKey('nvd_products.id'))
    nvd_products = relationship("NvdProduct", back_populates="nvd_cpe_matches")
    nvd_cpe_match_configurations = relationship("NvdCpeMatchConfiguration", back_populates="nvd_cpe_matches")