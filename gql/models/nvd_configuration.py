class NvdConfiguration(Base):
    __tablename__ = 'nvd_configurations'
    id = Column(String, primary_key=True)
    json_data = Column(String)
    date_updated = Column(DateTime)
    nvd_cpe_match_configurations = relationship("NvdCpeMatchConfiguration", back_populates="nvd_configurations")
    nvd_configurations_cve = relationship("NvdConfigurationsCve", back_populates="nvd_configurations")