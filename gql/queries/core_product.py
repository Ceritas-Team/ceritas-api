# Standard library imports
from sqlalchemy.orm import joinedload

# Third-party library imports
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from importlib import import_module

# Local application/library-specific imports
from ..models.core_label import CoreLabel
from ..models.core_product import CoreProduct
from ..models.core_product_component import CoreProductComponent
from ..models.core_product_organization import CoreProductOrganization
from ..models.core_rating_history import CoreRatingHistory
from ..models.vulnerability_core_product import VulnerabilityCoreProduct
from ..models.core_organization import CoreOrganization
from .core_label import CoreLabelNode
from .core_rating_history import CoreRatingHistoryNode
from .vulnerability import VulnerabilityNode

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
            'hbom',
            'current_rating_history_id',
            'uuid'
        )
        
    components = graphene.List(lambda: CoreProductNode)
    core_label = graphene.Field(lambda: CoreLabelNode)
    current_rating = graphene.Field(lambda: CoreRatingHistoryNode)
    organizations = graphene.Field('gql.queries.CoreOrganizationNode')
    vulnerabilities = graphene.List(lambda: VulnerabilityNode)
    components = graphene.List(lambda: CoreProductNode)

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
    
    def resolve_current_rating(self, info):
        current_rating_history_id = self.current_rating_history_id
        if not current_rating_history_id:
            return None
        return CoreRatingHistory.query.get(current_rating_history_id)
    
    def resolve_organizations(self, info):
        
        CoreOrganizationNode = import_module('.core_organization', '..models').CoreOrganizationNode
        # Use the core_product_organizations relationship to retrieve organizations
        return [product_organization.core_organization for product_organization in self.core_product_organizations]

    
    def resolve_vulnerabilities(self, info):
        vulnerability_core_products = VulnerabilityCoreProduct.query.filter_by(core_product_id=self.id).options(joinedload(VulnerabilityCoreProduct.vulnerability)).all()

        if not vulnerability_core_products:
            return []

        vulnerabilities = [vc_product.vulnerability for vc_product in vulnerability_core_products]

        if not vulnerabilities:
            return []

        return vulnerabilities
    
    @staticmethod
    def get(info):
        print("INFO", info)
        if 'id' in info.variable_values['input']:
            return CoreProduct.query.filter_by(id=info.variable_values['input']['id']).first()
        elif 'name' in info.variable_values['input']:
            return CoreProduct.query.filter_by(name=info.variable_values['input']['name']).first()
        elif 'uuid' in info.variable_values['input']:
            return CoreProduct.query.filter_by(uuid=info.variable_values['input']['uuid']).first()
        else:
            return CoreProduct.query.all()