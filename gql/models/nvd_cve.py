class NvdCve(Base):
    __tablename__ = 'nvd_cves'
    id = Column(String, primary_key=True)
    cve = Column(String)
    severity = Column(String)
    vulnerability = Column(String)
    mitigations = Column(String)
    mitigation_links = Column(String)
    jsondata = Column(String)
    date_published = Column(DateTime)
    date_modified = Column(DateTime)
    date_updated = Column(DateTime)
    nvd_configurations_cve = relationship("NvdConfigurationsCve", back_populates="nvd_cves")
    vulnerabilities = relationship("Vulnerability", back_populates="nvd_cves")