import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.core_label import CoreLabel

class CoreLabelNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreLabel
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'name', 
            'is_visible'
        )

    @staticmethod
    def get(info):
        query = CoreLabel.get_query(info)
        return query.all()