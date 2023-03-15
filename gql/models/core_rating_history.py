class CoreRatingHistory(Base):
    __tablename__ = 'core_rating_history'
    id = Column(String, primary_key=True)
    value = Column(String)
    algorithm_hash = Column(String)
    date_added = Column(DateTime)
    ratingable_type = Column(String)
    ratingable_id = Column(String, ForeignKey('core_organizations.id'))
    ratingable = relationship("CoreOrganization", back_populates="core_rating_history")
    core_organizations = relationship("CoreOrganization", back_populates="core_rating_history")
    core_products = relationship("CoreProduct", back_populates="core_rating_history")