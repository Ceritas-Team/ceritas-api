from ..models.group import Group
from .product_instance_group import ProductInstanceGroupNode
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
class GroupNode(SQLAlchemyObjectType):
    class Meta:
        model = Group
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'name', 
            'company_id', 
            'created_by', 
            'is_default', 
            'created_at', 
            'updated_at',
            'deleted_at',
            'product_instance_groups'
        )

    product_instance_groups = graphene.List(ProductInstanceGroupNode)
    
    def resolve_groups(self, info):
        if hasattr(self, 'id') and 'groups' in info.variable_values['input']:
            query = GroupNode.query.filter(groups=self.id)
            return query.all()
        return None
    
    @staticmethod
    def get(info):
        if 'id' in info.variable_values['input']:
            return Company.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return Company.query.all()