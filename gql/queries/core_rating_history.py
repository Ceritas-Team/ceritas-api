import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.core_rating_history import CoreRatingHistory

class CoreRatingHistoryNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreRatingHistory
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'value', 
            'date_added',
            'ratingable_type',
            'ratingable_id'
        )

    @staticmethod
    def get(info):
        query = CoreRatingHistory.get_query(info)
        return query.all()