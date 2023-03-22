from sqlalchemy import Column, DateTime, String, BigInteger, Text
from . import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class NvdCve(Base):
    __tablename__ = 'nvd_cves'
    id = Column(BigInteger, primary_key=True)
    cve = Column(String)
    severity = Column(String)
    vulnerability = Column(Text)
    mitigations = Column(Text)
    mitigation_links = Column(Text)
    jsondata = Column(JSONB)
    date_published = Column(DateTime)
    date_modified = Column(DateTime)
    date_updated = Column(DateTime)
    #nvd_configurations_cve = relationship("NvdConfigurationsCve", back_populates="nvd_cves")
    vulnerabilities = relationship('Vulnerability', backref='nvd_cve')