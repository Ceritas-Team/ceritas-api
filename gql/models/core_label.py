class CoreLabel(Base):
    __tablename__ = 'core_labels'
    id = Column(String, primary_key=True)
    name = Column(String)
    is_visible = Column(Boolean)
    core_products = relationship("CoreProduct", back_populates="core_labels")