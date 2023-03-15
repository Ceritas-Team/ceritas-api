# import os
# from sqlalchemy import create_engine
# from sqlalchemy import Column, Integer, String, DateTime, create_engine ,inspect, MetaData, Boolean, ForeignKey, Enum
# from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
# from sqlalchemy.ext.declarative import declarative_base

# host = os.environ['DB_HOST']
# user = os.environ['DB_USER']
# password = os.environ['DB_PASSWORD']
# database = os.environ['DB_NAME']
# db_url = f"postgresql://{user}:{password}@{host}/{database}"
# engine = create_engine(db_url, convert_unicode=True)

# session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Base = declarative_base()

# Base.query = session.query_property()

# metadata = MetaData()
# # metadata.reflect(engine, only=['nvd_vendors'])

# class NvdVendor(Base):
#     __tablename__ = 'nvd_vendors'
#     id = Column(String, primary_key=True)
#     cpe_vendor = Column(String)
#     date_updated = Column(DateTime)
#     organization_id = Column(String, ForeignKey('core_organizations.id'))
#     nvd_products = relationship("NvdProduct", back_populates="nvd_vendors")
#     core_organizations = relationship("CoreOrganization", back_populates="nvd_vendors")

# class NvdProduct(Base):
#     __tablename__ = 'nvd_products'
#     id = Column(String, primary_key=True)
#     cpe_short_product = Column(String)
#     cpe_product_name = Column(String)
#     date_updated = Column(DateTime)
#     date_link = Column(DateTime)
#     core_product_id = Column(String, ForeignKey('core_products.id'))
#     nvd_vendor_id = Column(String, ForeignKey('nvd_vendors.id'))
#     nvd_vendors = relationship("NvdVendor", back_populates="nvd_products") 
#     nvd_cpe_matches = relationship("NvdCpeMatch", back_populates="nvd_products")
#     core_products = relationship("CoreProduct", back_populates="nvd_products")
      
# class NvdCpeMatch(Base):
#     __tablename__ = 'nvd_cpe_matches'
#     id = Column(String, primary_key=True)
#     cpe = Column(String)
#     date_upated = Column(DateTime)
#     version_json = Column(String)
#     nvd_product_id = Column(String, ForeignKey('nvd_products.id'))
#     nvd_products = relationship("NvdProduct", back_populates="nvd_cpe_matches")
#     nvd_cpe_match_configurations = relationship("NvdCpeMatchConfiguration", back_populates="nvd_cpe_matches")
    
# class NvdCpeMatchConfiguration(Base):
#     __tablename__='nvd_cpe_match_configurations'
#     nvd_cpe_match_id = Column(String, ForeignKey('nvd_cpe_matches.id'), primary_key=True)
#     nvd_configuration_id = Column(String, ForeignKey('nvd_configurations.id'), primary_key=True)
#     nvd_configurations = relationship("NvdConfiguration", back_populates="nvd_cpe_match_configurations")
#     nvd_cpe_matches = relationship("NvdCpeMatch", back_populates="nvd_cpe_match_configurations")
 
# class NvdConfiguration(Base):
#     __tablename__ = 'nvd_configurations'
#     id = Column(String, primary_key=True)
#     json_data = Column(String)
#     date_updated = Column(DateTime)
#     nvd_cpe_match_configurations = relationship("NvdCpeMatchConfiguration", back_populates="nvd_configurations")
#     nvd_configurations_cve = relationship("NvdConfigurationsCve", back_populates="nvd_configurations")
    
# class NvdConfigurationsCve(Base):
#     __tablename__ = 'nvd_configurations_cve'
#     date_updated = Column(DateTime)
#     nvd_configuration_id = Column(String, ForeignKey('nvd_configurations.id'), primary_key=True)
#     nvd_cve_id = Column(String, ForeignKey('nvd_cves.id'), primary_key=True)
#     nvd_configurations = relationship("NvdConfiguration", back_populates="nvd_configurations_cve")
#     nvd_cves = relationship("NvdCve", back_populates="nvd_configurations_cve")
    
# class NvdCve(Base):
#     __tablename__ = 'nvd_cves'
#     id = Column(String, primary_key=True)
#     cve = Column(String)
#     severity = Column(String)
#     vulnerability = Column(String)
#     mitigations = Column(String)
#     mitigation_links = Column(String)
#     jsondata = Column(String)
#     date_published = Column(DateTime)
#     date_modified = Column(DateTime)
#     date_updated = Column(DateTime)
#     nvd_configurations_cve = relationship("NvdConfigurationsCve", back_populates="nvd_cves")
#     vulnerabilities = relationship("Vulnerability", back_populates="nvd_cves")
    
# class Vulnerability(Base):
#     __tablename__ = 'vulnerabilities'
#     id = Column(String, primary_key=True)
#     cer_id = Column(String)
#     cve_reserved = Column(Boolean)
#     ics_cert_number = Column(String)
#     vendor_vulnerability_id = Column(String)
#     raw_mitigation_description = Column(String)
#     curated_mitigation_description = Column(String)
#     attack_complexity = Column(String)
#     cwe = Column(String)
#     cvss_score = Column(String)
#     date_released = Column(DateTime)
#     dated_added = Column(DateTime)
#     dated_updated = Column(DateTime)
#     current_severity_history_id = Column(String, ForeignKey('vulnerability_severity_history.id'))
#     cve_id = Column(String, ForeignKey('nvd_cves.id'))
#     vulnerability_severity_history = relationship("VulnerabilitySeverityHistory", back_populates="vulnerabilities")
#     nvd_cves = relationship("NvdCve", back_populates="vulnerabilities")
#     product_instance_mitigations = relationship("ProductInstanceMitigation", back_populates="vulnerabilities")
#     vulnerability_core_product = relationship("VulnerabilityCoreProduct", back_populates="vulnerabilities")
  
# class VulnerabilityCoreProduct(Base):
#     __tablename__ = 'vulnerability_core_product'
#     user_id = Column(String)
#     note = Column(String)
#     is_visible = Column(Boolean)
#     date_added = Column(DateTime)
#     vulnerability_id = Column(String, ForeignKey('vulnerabilities.id'), primary_key=True)
#     core_product_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
#     vulnerabilities = relationship("Vulnerability", back_populates="vulnerability_core_product")
#     core_products = relationship("CoreProduct", back_populates="vulnerability_core_product")
    
# class VulnerabilitySeverityHistory(Base):
#     __tablename__ = 'vulnerability_severity_history'
#     id = Column(String, primary_key=True)
#     vulnerability_id = Column(String)
#     value = Column(String)
#     date_added = Column(DateTime)
#     vulnerabilities = relationship("Vulnerability", back_populates="vulnerability_severity_history")
    
# class NvdLink(Base):
#     __tablename__ = 'nvd_linked'
#     id = Column(String, primary_key=True)
#     linkable_type = Column(String)
#     linkable_id = Column(String, ForeignKey('core_products.id'))
#     date_moderated = Column(DateTime)
#     date_linked = Column(DateTime)
#     best_match = Column(String)
#     core_products = relationship("CoreProduct", back_populates="nvd_linked")
    
# class CoreProductComponent(Base):
#     __tablename__ = 'core_product_component'
#     parent_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
#     child_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
#     child = relationship("CoreProduct", foreign_keys=[child_id], back_populates="core_product_component")
#     parent = relationship("CoreProduct", foreign_keys=[parent_id], back_populates="core_product_component")
    
# class CoreRatingHistory(Base):
#     __tablename__ = 'core_rating_history'
#     id = Column(String, primary_key=True)
#     value = Column(String)
#     algorithm_hash = Column(String)
#     date_added = Column(DateTime)
#     ratingable_type = Column(String)
#     ratingable_id = Column(String, ForeignKey('core_organizations.id'))
#     ratingable = relationship("CoreOrganization", back_populates="core_rating_history")
#     core_organizations = relationship("CoreOrganization", back_populates="core_rating_history")
#     core_products = relationship("CoreProduct", back_populates="core_rating_history")
    
# class CoreProduct(Base):
#     __tablename__='core_products'
#     id = Column(String, primary_key=True)
#     type = Enum('product', 'component', name='type')
#     category = Enum('IT', 'OT', name='category')
#     img_link = Column(String)
#     jsondata = Column(String)
#     name = Column(String)
#     label_id = Column(String, ForeignKey('core_labels.id'))
#     core_labels = relationship("CoreLabel", back_populates="core_products")
#     current_rating_history_id = Column(String, ForeignKey('core_rating_history.id'))
#     core_rating_history = relationship("CoreRatingHistory", back_populates="core_products")
#     product_instances = relationship("ProductInstance", back_populates="core_products")
#     core_product_organizations = relationship("CoreProductOrganization", back_populates="core_products")
#     vulnerability_core_product = relationship("VulnerabilityCoreProduct", back_populates="core_products")
#     nvd_products = relationship("NvdProduct", back_populates="core_products")
#     product_instances = relationship("ProductInstance", back_populates="core_products")
#     nvd_linked = relationship("NvdLink", back_populates="core_products")
#     core_product_component = relationship("CoreProductComponent", foreign_keys=[CoreProductComponent.parent_id], back_populates="parent")
#     core_rating_history = relationship("CoreRatingHistory", back_populates="core_products")
#     company_product = relationship("CompanyProduct", back_populates="core_products")
    
# class CoreProductOrganization(Base):
#     __tablename__ = 'core_product_organizations'
#     product_id = Column(String, ForeignKey('core_products.id'), primary_key=True)
#     organization_id = Column(String, ForeignKey('core_organizations.id'), primary_key=True)
#     core_organizations = relationship("CoreOrganization", back_populates="core_product_organizations")
#     relationship = Enum('relationship', 'made_by', name='relationship')
#     core_products = relationship("CoreProduct", back_populates="core_product_organizations")
    
# class CoreLabel(Base):
#     __tablename__ = 'core_labels'
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     is_visible = Column(Boolean)
#     core_products = relationship("CoreProduct", back_populates="core_labels")

# class CoreOrganization(Base):
#     __tablename__ = 'core_organizations'
#     id = Column(String, primary_key=True)
#     uuid = Column(String)
#     name = Column(String)
#     img_link = Column(String)
#     jsondata = Column(String)
#     core_product_organizations = relationship("CoreProductOrganization", back_populates="core_organizations")
#     core_rating_history = relationship("CoreRatingHistory", back_populates="core_organizations")
#     core_risks_history = relationship("CoreRisksHistory", back_populates="core_organizations")
#     nvd_vendors = relationship("NvdVendor", back_populates="core_organizations")
    
# class CoreRisksHistory(Base):
#     __tablename__ = 'core_risks_history'
#     id = Column(String, primary_key=True)
#     organization_id = Column(String, ForeignKey('core_organizations.id'))
#     risk_type = Enum('risk', 'threat', name='risk_type')
#     value = Column(String)
#     date_added = Column(DateTime) 
#     core_organizations = relationship("CoreOrganization", back_populates="core_risks_history")
    
# class ProductInstanceMitigation(Base):
#     __tablename__ = 'product_instance_mitigations'
#     id = Column(String, primary_key=True)
#     product_instance_id = Column(String, ForeignKey('product_instances.id'))
#     status = Column(String)
#     note = Column(String)
#     date_added = Column(DateTime)
#     date_mitigated = Column(DateTime)
#     vulnerability_id = Column(String, ForeignKey('vulnerabilities.id'))
#     vulnerabilities = relationship("Vulnerability", back_populates="product_instance_mitigations")
#     product_instances = relationship("ProductInstance", back_populates="product_instance_mitigations")
    
# class ProductInstance(Base):
#     __tablename__ = 'product_instances'
#     id = Column(String, primary_key=True)
#     product_id = Column(String, ForeignKey('product_instance_group.id'))
#     parent_instance_id = Column(String)
#     date_added = Column(DateTime)
#     core_product_id = Column(String, ForeignKey('core_products.id'))
#     core_products = relationship("CoreProduct", back_populates="product_instances")
#     product_instance_mitigations = relationship("ProductInstanceMitigation", back_populates="product_instances")
#     product_instance_group = relationship("ProductInstanceGroup", back_populates="product_instances")
    
# class ProductInstanceGroup(Base):
#     __tablename__ = 'product_instance_group'
#     id = Column(String, primary_key=True)
#     group_id = Column(String, ForeignKey('groups.id'))
#     date_added = Column(DateTime)
#     groups = relationship("Group", back_populates="product_instance_group")
#     product_instances = relationship("ProductInstance", back_populates="product_instance_group")
    
# class Company(Base):
#     __tablename__ = 'companies'
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     description = Column(String)
#     website = Column(String)
#     address_1 = Column(String)
#     address_2 = Column(String)
#     city = Column(String)
#     state = Column(String)
#     zip = Column(String)
#     country = Column(String)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     company_product = relationship("CompanyProduct", back_populates="company")
#     company_location = relationship("CompanyLocation", back_populates="company")
#     groups = relationship("Group", back_populates="company")
    
# class CompanyProduct(Base):
#     __tablename__ = 'company_product'
#     id = Column(String, primary_key=True)
#     company_id = Column(String, ForeignKey('companies.id'))
#     core_product_id = Column(String, ForeignKey('core_products.id'))
#     date_added = Column(DateTime)
#     instances = relationship("Instance", back_populates="company_product")
#     company = relationship("Company", back_populates="company_product")
#     core_products = relationship("CoreProduct", back_populates="company_product")
    
# class InstanceMitigation(Base):
#     __tablename__ = 'instance_mitigations'
#     id = Column(String, primary_key=True)
#     product_instance_id = Column(String, ForeignKey('product_instances.id'))
#     vulnerability_id = Column(String, ForeignKey('vulnerabilities.id'))
#     status = Column(String)
#     note = Column(String)
#     instance_id = Column(String, ForeignKey('instances.id'))
#     date_added = Column(DateTime)
#     date_mitigated = Column(DateTime)
#     instances = relationship("Instance", back_populates="instance_mitigations")
    
# class Instance(Base):
#     __tablename__ = 'instances'
#     id = Column(String, primary_key=True)
#     company_product_id = Column(String, ForeignKey('company_product.id'))
#     location_id = Column(String, ForeignKey('company_location.id'))
#     company_asset_id = Column(String)
#     date_added = Column(DateTime)
#     company_product = relationship("CompanyProduct", back_populates="instances")
#     company_location = relationship("CompanyLocation", back_populates="instances")
#     instance_group = relationship("InstanceGroup", back_populates="instances")
#     instance_mitigations = relationship("InstanceMitigation", back_populates="instances")
    
# class InstanceGroup(Base):
#     __tablename__ = 'instance_group'
#     id = Column(String, primary_key=True)
#     date_added = Column(DateTime)
#     instance_id = Column(String, ForeignKey('instances.id'))
#     group_id = Column(String, ForeignKey('groups.id'))
#     groups = relationship("Group", foreign_keys=[group_id],back_populates="instance_group")
#     instances = relationship("Instance", foreign_keys=[instance_id], back_populates="instance_group")
    
# class CompanyLocation(Base):
#     __tablename__ = 'company_location'
#     id = Column(String, primary_key=True)
#     name = Column(String)
#     company_id = Column(String, ForeignKey('companies.id'))
#     company = relationship("Company", back_populates="company_location")
#     instances = relationship("Instance", back_populates="company_location")    
   
# class Group(Base):
#     __tablename__ = 'groups'
#     id = Column(String, primary_key=True)
#     product_instance_group = relationship("ProductInstanceGroup", back_populates="groups")
#     instance_group = relationship("InstanceGroup", back_populates="groups")
#     name = Column(String)
#     company_id = Column(String, ForeignKey('companies.id'))
#     company = relationship("Company", back_populates="groups")
#     created_by = Column(String)
#     is_default = Column(Boolean)
#     created_at = Column(DateTime)
#     updated_at = Column(DateTime)
#     deleted_at = Column(DateTime)
    
# Models = [ 
#     NvdVendor, 
#     NvdProduct, 
#     NvdCpeMatch, 
#     NvdCpeMatchConfiguration, 
#     NvdConfiguration, 
#     NvdConfigurationsCve, 
#     NvdCve, 
#     Vulnerability, 
#     VulnerabilitySeverityHistory, 
#     NvdLink, 
#     CoreProductComponent, 
#     CoreProduct, 
#     CoreProductOrganization, 
#     CoreRatingHistory, 
#     CoreLabel, 
#     CoreOrganization, 
#     CoreRisksHistory, 
#     ProductInstanceMitigation, 
#     ProductInstance, 
#     ProductInstanceGroup, 
#     Company, 
#     CompanyProduct, 
#     Instance, 
#     InstanceGroup, 
#     CompanyLocation, 
#     InstanceMitigation, 
#     Group
# ]