from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import graphene
import json
from ..models.core_product_component import CoreProductComponent
class CoreProductComponentNode(SQLAlchemyObjectType):
    name = graphene.String()

    class Meta:
        model = CoreProductComponent
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'parent_id',
            'child_id',
        )

    def resolve_name(self, info):
        component = info.context['components_map'].get(self.child_id)
        return component.name if component else None