from ..models.core_product_organization import CoreProductOrganization
from ..models.core_product import CoreProduct
from ..models.core_organization import CoreOrganization
from .core_product import CoreProductNode
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
import json

class CoreOrganizationNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreOrganization
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id',
            'uuid',
            'name',
            'jsondata',
            'core_products',
            # 'core_rating_his'
        )
        
    core_products = graphene.List(CoreProductNode)
    
    def resolve_core_products(self, info):
        # from importlib import import_module
        # CoreProductNode = import_module('.core_product', '..queries').CoreProductNode
        
        core_products = (
            CoreProduct.query
            .join(CoreProductOrganization, CoreProductOrganization.product_id == CoreProduct.id)
            .filter(CoreProductOrganization.organization_id == self.id)
            .all()
        )
        return core_products
    
    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return CoreOrganization.query.filter_by(id=info.variable_values['input']['id']).first()
        if 'name' in info.variable_values['input']:
            return CoreOrganization.query.filter_by(id=info.variable_values['input']['name']).first()
        else:
            return CoreOrganization.query.all()

