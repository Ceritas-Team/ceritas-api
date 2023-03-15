class InstanceMitigation(Base):
    __tablename__ = 'instance_mitigations'
    id = Column(String, primary_key=True)
    product_instance_id = Column(String, ForeignKey('product_instances.id'))
    vulnerability_id = Column(String, ForeignKey('vulnerabilities.id'))
    status = Column(String)
    note = Column(String)
    instance_id = Column(String, ForeignKey('instances.id'))
    date_added = Column(DateTime)
    date_mitigated = Column(DateTime)
    instances = relationship("Instance", back_populates="instance_mitigations")