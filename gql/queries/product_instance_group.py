from .product_instance import ProductInstanceNode
from ..models.product_instance import ProductInstance
from ..models.product_instance_group import ProductInstanceGroup
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

class ProductInstanceGroupNode(SQLAlchemyObjectType):
    class Meta:
        model = ProductInstanceGroup
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'product_instance_id',
            'group_id',
            'date_added'
        )
        
    product_instances = graphene.List(lambda: ProductInstanceNode)
    
    def resolve_product_instances(self, info):
        if id: 
            query = ProductInstance.query.filter(id=id)
        else:
            query = ProductInstance.query.all()
        return query
        
    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return ProductInstanceGroup.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return ProductInstanceGroup.query.all()
