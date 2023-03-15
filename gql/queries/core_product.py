
from ..models.core_product import CoreProduct
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
from ..models.core_product_component import CoreProductComponent
from .core_product_component import CoreProductComponentNode

class ComponentNode(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
class CoreProductNode(SQLAlchemyObjectType):
    class Meta:
        model = CoreProduct
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'type',
            'category', 
            'img_link',
            'jsondata',
            'name',
            'label_id'
        )
        
    components = graphene.List(lambda: ComponentNode)

    def resolve_components(self, info):
        components_relationship = (
            CoreProductComponent.query
            .filter(CoreProductComponent.parent_id == self.id)
            .all()
        )

        child_ids = [relationship.child_id for relationship in components_relationship]
        child_components = CoreProduct.query.filter(CoreProduct.id.in_(child_ids)).all()
        components_map = {component.id: component for component in child_components}

        components_result = [
            ComponentNode(id=component_map.id, name=component_map.name)
            for component_map in components_map.values()
        ]

        return components_result
    
    @staticmethod
    def get(info):
        print("INFO", info)
        if 'id' in info.variable_values['input']:
            return CoreProduct.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return CoreProduct.query.all()