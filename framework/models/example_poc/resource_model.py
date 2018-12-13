import datetime

from sqlalchemy import TIMESTAMP, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class ResourceModel(BaseModel):
    __tablename__ = 'resources'

    id = Column('id', Integer, primary_key=True)
    dag_id = Column('dag_id', String(255), default='', nullable=False)
    resource_id = Column('resource_id', String(255), default='', nullable=False)
    status = Column('status', String(255), default='', nullable=False)
    path = Column('path', String(255), default='', nullable=False)
    contents = Column('contents', JSON, default='')
    created_at = Column('created_at', TIMESTAMP, default=datetime.datetime.utcnow, nullable=False)
    updated_at = Column('updated_at', TIMESTAMP, onupdate=datetime.datetime.utcnow)
