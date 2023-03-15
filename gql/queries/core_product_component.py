from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
import json
from ..models.core_product_component import CoreProductComponent
class CoreProductComponentNode(SQLAlchemyObjectType):
    
    
    class Meta:
        model = CoreProductComponent
        interfaces = (graphene.relay.Node,)
        # Add the fields you want to expose in your GraphQL API, e.g., 'id', 'name'
