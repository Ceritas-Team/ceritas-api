from sqlalchemy import Column, String, DateTime, ForeignKey, BigInteger, Integer
from . import Base
from sqlalchemy.orm import relationship

class CoreRatingHistory(Base):
    __tablename__ = 'core_rating_history'
    id = Column(BigInteger, primary_key=True)
    value = Column(Integer)
    #algorithm_hash = Column(String)
    date_added = Column(DateTime)
    ratingable_type = Column(String)
    ratingable_id = Column(BigInteger)
    #core_organizations = relationship("CoreOrganization", backref="core_rating_history")
    core_products = relationship("CoreProduct", backref="core_rating_history", uselist=False)