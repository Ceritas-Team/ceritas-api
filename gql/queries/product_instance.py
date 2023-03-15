from ..models.product_instance import ProductInstance
from ..models.product_instance_group import ProductInstanceGroup
from ..models.core_product import CoreProduct
from .core_product import CoreProductNode
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene

class ProductInstanceNode(SQLAlchemyObjectType):
    class Meta:
        model = ProductInstance
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'product_id',
            'parent_instance_id',
            'date_added'
        )
        
    product_instances = graphene.List(lambda: ProductInstanceNode)
    core_products = graphene.List(CoreProductNode)
    
    def resolve_core_products(self, info):
        if id: 
            query = CoreProduct.query.filter(id=id)
        else:
            query = CoreProduct.query.all()
        return query
        
    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return ProductInstance.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return ProductInstance.query.all()
