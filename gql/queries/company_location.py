from ..models import CompanyLocation

class CompanyLocationNode(SQLAlchemyObjectType):
    class Meta:
        model = CompanyLocation
        interfaces = (graphene.relay.Node,)
        only_fields = ('id', 'name', 'company_id', 'company', 'instances')

    @staticmethod
    def get(info):
        return CompanyLocation.query