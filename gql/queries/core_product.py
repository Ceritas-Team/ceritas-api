
from ..models.core_product import CoreProduct
from graphene_sqlalchemy import SQLAlchemyObjectType
import graphene
from ..models.core_product_component import CoreProductComponent
from ..models.core_label import CoreLabel
from .core_label import CoreLabelNode

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
            'label_id',
            'hbom'
        )
        
    components = graphene.List(lambda: CoreProductNode)
    core_label = graphene.Field(lambda: CoreLabelNode)

    def resolve_components(self, info):
        components_relationship = (
            CoreProductComponent.query
            .filter(CoreProductComponent.parent_id == self.id)
            .all()
        )

        child_ids = [relationship.child_id for relationship in components_relationship]
        child_components = CoreProduct.query.filter(CoreProduct.id.in_(child_ids)).all()

        return child_components
    
    def resolve_core_label(self, info):
       label_id = self.label_id
       if not label_id:
           return None
       return CoreLabel.query.get(label_id)
    
    @staticmethod
    def get(info):
        print("INFO", info)
        if 'id' in info.variable_values['input']:
            return CoreProduct.query.filter_by(id=info.variable_values['input']['id']).first()
        else:
            return CoreProduct.query.all()