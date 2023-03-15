

class ProductInstanceMitigation(Base):
    __tablename__ = 'product_instance_mitigations'
    id = Column(String, primary_key=True)
    product_instance_id = Column(String, ForeignKey('product_instances.id'))
    status = Column(String)
    note = Column(String)
    date_added = Column(DateTime)
    date_mitigated = Column(DateTime)
    vulnerability_id = Column(String, ForeignKey('vulnerabilities.id'))
    vulnerabilities = relationship("Vulnerability", back_populates="product_instance_mitigations")
    product_instances = relationship("ProductInstance", back_populates="product_instance_mitigations")