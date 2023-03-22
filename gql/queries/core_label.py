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

    core_products = graphene.List('gql.queries.CoreProductNode')

    def resolve_core_labels(self, info):
        return self.core_products

    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return CoreLabel.query.filter_by(id=info.variable_values['input']['id']).first()
        if 'name' in info.variable_values['input']:
            return CoreLabel.query.filter_by(id=info.variable_values['input']['name']).first()
        else:
            return CoreLabel.query.all()