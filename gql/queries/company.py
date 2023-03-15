from ..models.company import Company
from ..models.product_instance_group import ProductInstanceGroup
from ..models.product_instance import ProductInstance
from ..models.group import Group
from ..models.core_product import CoreProduct
from .group import GroupNode
from .core_product import CoreProductNode
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
import json
class CompanyNode(SQLAlchemyObjectType):
    class Meta:
        model = Company
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'name', 
            'description', 
            'website', 
            'address_1', 
            'address_2', 
            'city',
            'state',
            'zip',
            'country',
            'created_at',
            'updated_at',
            'company_product',
            'company_location',
            'groups'
        )
        
    core_products = graphene.List(lambda: CoreProductNode)
    
    def resolve_core_products(self, info):
        core_products = (
            CoreProduct.query
            .join(ProductInstance, ProductInstance.product_id == CoreProduct.id)
            .join(ProductInstanceGroup, ProductInstanceGroup.product_instance_id == ProductInstance.id)
            .join(Group, Group.id == ProductInstanceGroup.group_id)
            .filter(Group.company_id == self.id)
            .all()
        )
        return core_products

        
    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return Company.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return Company.query.all()
    
def map_core_product_to_node(core_product):
    # Define a function to map a CoreProduct instance to a CoreProductNode instance
    return CoreProductNode(
        id=core_product.id,
        name=core_product.name,
        img_link=core_product.img_link,
        jsondata=json.loads(core_product.jsondata),
        label_id=core_product.label_id
    )