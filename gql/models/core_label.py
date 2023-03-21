from sqlalchemy import Column, BigInteger, String, Boolean
#from sqlalchemy.orm import relationship 
from . import Base

class CoreLabel(Base):
    __tablename__ = 'core_labels'

    id = Column(BigInteger, primary_key=True)
    name = Column(String, nullable=False)
    is_visible = Column(Boolean, nullable=False, default=True)