from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship, backref)
from sqlalchemy import Column, Integer, String, DateTime, create_engine ,inspect, MetaData, Boolean, ForeignKey, Enum

import os
from sqlalchemy import create_engine

# host = os.environ['DB_HOST']
# user = os.environ['DB_USER']
# password = os.environ['DB_PASSWORD']
# database = os.environ['DB_NAME']
db_url = f"postgresql://bill:S1kaUjOt3hrC@ep-summer-haze-591455.us-east-2.aws.neon.tech/ceritas"
engine = create_engine(db_url, convert_unicode=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()

Base.query = session.query_property()

metadata = MetaData()

from .company import Company