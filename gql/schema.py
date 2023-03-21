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
from .models import CoreOrganization

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # nvd_vendors = graphene.List(NvdVendor)
    companies = graphene.List(
        lambda:CompanyNode, 
        id=graphene.String(),
        name=graphene.String()
    )
    
    core_organizations = graphene.List(
        lambda:CoreOrganizationNode, 
        id=graphene.String(),
        name=graphene.String(),
    )

    def resolve_companies(self, info, id=None, name=None):
        query = Company.query
        if id:
            query = query.filter(Company.id == id)
        if name:
            query = query.filter(Company.name == name)
        return query.all()
    
    def resolve_core_organizations(self, info, id=None, name=None, org_id=None):
        query = CoreOrganization.query
        if id:
            query = query.filter(CoreOrganization.id == id)
        if name:
            query = query.filter(CoreOrganization.name == name)
        return query.all()
    
schema = graphene.Schema(query=Query)