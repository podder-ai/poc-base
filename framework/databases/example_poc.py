from sqlalchemy import create_engine
# from sqlalchemy.engine.base import Engine
# from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

from framework.settings import POC_DATABASE_URL

Engine = create_engine(POC_DATABASE_URL, echo=True)

sessionmaker(bind=Engine)
