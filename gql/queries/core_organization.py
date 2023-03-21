import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.core_organization import CoreOrganization

class CoreOrganizationNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreOrganization
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id',
            'uuid',
            'name',
            'jsondata',
            #'core_risks_history',
        )

    @staticmethod
    def get(info):
        return CoreOrganization.query
