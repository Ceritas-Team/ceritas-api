from sqlalchemy import Column, String, BigInteger, Text, JSON, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from . import Base

class CoreOrganization(Base):
    __tablename__ = 'core_organizations'
    id = Column(BigInteger, primary_key=True)
    uuid = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), nullable=False, index=True)
    img_link = Column(Text)
    jsondata = Column(JSON)
    neo4j_node_id = Column(BigInteger, index=True)
    neo4j_type = Column(String(255), nullable=False)

    # Relationships
    # Assuming you have defined the CoreProductOrganization and CoreRisksHistory models
    core_product_organizations = relationship("CoreProductOrganization", back_populates="core_organization")
    #core_risks_history = relationship("CoreRisksHistory", backref="core_organization")

    # Check constraint
    __table_args__ = (
        CheckConstraint(neo4j_type.in_(['manufacturer', 'organization', 'manufacturer_organization'])),
    )