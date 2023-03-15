class NvdLink(Base):
    __tablename__ = 'nvd_linked'
    id = Column(String, primary_key=True)
    linkable_type = Column(String)
    linkable_id = Column(String, ForeignKey('core_products.id'))
    date_moderated = Column(DateTime)
    date_linked = Column(DateTime)
    best_match = Column(String)
    core_products = relationship("CoreProduct", back_populates="nvd_linked")