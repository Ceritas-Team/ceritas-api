class NvdConfigurationsCve(Base):
    __tablename__ = 'nvd_configurations_cve'
    date_updated = Column(DateTime)
    nvd_configuration_id = Column(String, ForeignKey('nvd_configurations.id'), primary_key=True)
    nvd_cve_id = Column(String, ForeignKey('nvd_cves.id'), primary_key=True)
    nvd_configurations = relationship("NvdConfiguration", back_populates="nvd_configurations_cve")
    nvd_cves = relationship("NvdCve", back_populates="nvd_configurations_cve")