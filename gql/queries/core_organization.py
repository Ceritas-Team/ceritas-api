from ..models import CoreOrganization

class CoreOrganizationNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreOrganization
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'uuid',
            'name',
            'jsondata',
            'core_product_organization',
            'core_rating_his'
        )

    @staticmethod
    def get(info):
        return CoreOrganization.query