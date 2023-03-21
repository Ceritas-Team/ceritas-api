

class CompanyLocation(Base):
    __tablename__ = 'company_location'
    id = Column(String, primary_key=True)
    name = Column(String)
    company_id = Column(String, ForeignKey('companies.id'))
    company = relationship("Company", back_populates="company_location")
    instances = relationship("Instance", back_populates="company_location")    