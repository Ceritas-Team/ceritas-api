class NvdCpeMatchConfiguration(Base):
    __tablename__='nvd_cpe_match_configurations'
    nvd_cpe_match_id = Column(String, ForeignKey('nvd_cpe_matches.id'), primary_key=True)
    nvd_configuration_id = Column(String, ForeignKey('nvd_configurations.id'), primary_key=True)
    nvd_configurations = relationship("NvdConfiguration", back_populates="nvd_cpe_match_configurations")
    nvd_cpe_matches = relationship("NvdCpeMatch", back_populates="nvd_cpe_match_configurations")