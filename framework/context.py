from .config import Config
from .logger import Logger
from .file import File


class Context(object):
    def __init__(self, dag_id:str) -> None:
        self.logger = Logger()
        self.config = Config()
        self.file = File()
        self.dag_id = dag_id
