from . import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Enum, Boolean
from sqlalchemy.orm import relationship
# from .instance import Instance
from .group import Group
class InstanceGroup(Base):
    __tablename__ = 'instance_group'
    id = Column(String, primary_key=True)
    date_added = Column(DateTime)
    instance_id = Column(String, ForeignKey('instances.id'))
    group_id = Column(String, ForeignKey('groups.id'))
    groups = relationship("Group", foreign_keys=[group_id],back_populates="instance_group")
    instances = relationship("Instance", foreign_keys=[instance_id], back_populates="instance_group")