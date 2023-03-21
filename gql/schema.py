import os
import json
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base
from .queries.company import CompanyNode
from .queries.core_organization import CoreOrganizationNode
from .models import Company

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # nvd_vendors = graphene.List(NvdVendor)
    companies = graphene.List(lambda:CompanyNode, id=graphene.String())
    
    core_organizations = graphene.List(lambda:CoreOrganizationNode, id=graphene.String())

    def resolve_companies(self, info, id=None):
        if id:
            query = Company.query.filter(Company.id == id).all()
        else:
            query = Company.query.all()
        return query
    
    def resolve_core_organizations(self, info, id=None):
        if id:
            query = CoreOrganization.query.filter(CoreOrganization.id == id).all()
        else:
            query = CoreOrganization.query.all()
        return query
    
schema = graphene.Schema(query=Query)