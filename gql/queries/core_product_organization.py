import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.core_product_organization import CoreProductOrganization

class CoreProductOrganizationNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreProductOrganization
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'product_id',
            'organization_id',
            'relation',
            'core_product',
            'core_organization',
        )

    @staticmethod
    def get(info):
        return CoreProductOrganization.query
