from ..models import CoreLabel

class CoreLabelNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreLabel
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'name', 
            'is_visible',
            'core_products'
        )

    @staticmethod
    def get(info):
        return CoreLabel.query