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
from .queries.core_product import CoreProductNode
from .queries.core_label import CoreLabelNode
from .models import Company
from .models import CoreOrganization
from .models import CoreProduct
from .models import CoreLabel

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

    core_products = graphene.List(
        lambda:CoreProductNode,
        id=graphene.String(),
        name=graphene.String(),
        uuid=graphene.String(),
    )

    core_labels = graphene.List(
        lambda:CoreLabelNode,
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

    def resolve_core_products(self, info, id=None, uuid=None, name=None):
        query = CoreProduct.query
        if id:
            query = query.filter(CoreProduct.id == id)
        if uuid:
            query = query.filter(CoreProduct.uuid == uuid)
        if name:
            query = query.filter(CoreProduct.name == name)
        return query.all()
    
    def resolve_core_labels(self, info, id=None, name=None):
        query = CoreLabel.query
        if id:
            query = query.filter(CoreLabel.id == id)
        if name:
            query = query.filter(CoreLabel.name == name)
        return query.all()
    
schema = graphene.Schema(query=Query)