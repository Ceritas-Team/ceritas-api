from ..models import CompanyProduct

class CompanyProductNode(SQLAlchemyObjectType):
    class Meta:
        model = CompanyProduct
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id', 
            'company_id', 
            'core_product_id', 
            'date_added', 
            'instances', 
            'company', 
            'core_products'
        )

    @staticmethod
    def get(info):
        return CompanyProduct.query