from framework.settings import POC_DATABASE_URL
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import sessionmaker

engine: Engine = create_engine(POC_DATABASE_URL, echo=True)

Session: DeclarativeMeta = sessionmaker(bind=engine)
