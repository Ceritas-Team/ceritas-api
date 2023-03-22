import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from ..models.nvd_cve import NvdCve

class NvdCveNode(SQLAlchemyObjectType):
    class Meta:
        model = NvdCve
        interfaces = (graphene.relay.Node,)
        only_fields = (
            'id',
            'cve',
            'severity',
            'vulnerability',
            'mitigations',
            'mitigation_links',
            'jsondata',
            'date_published',
            'date_modified',
            'date_updated',
            'mitigation_toast'
        )

    @staticmethod
    def get(info, id=None, cve=None):
        query = NvdCve.query

        if id is not None:
            query = query.filter_by(id=id)

        if cve is not None:
            query = query.filter_by(cve=cve)

        return query.all()