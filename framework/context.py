from .config import Config
from .logger import Logger
from .file import File


class Context(object):
    def __init__(self):
        self.logger = Logger()
        self.config = Config()
        self.file = File()
