class CoreRisksHistory(Base):
    __tablename__ = 'core_risks_history'
    id = Column(String, primary_key=True)
    organization_id = Column(String, ForeignKey('core_organizations.id'))
    risk_type = Enum('risk', 'threat', name='risk_type')
    value = Column(String)
    date_added = Column(DateTime) 
    core_organizations = relationship("CoreOrganization", back_populates="core_risks_history")