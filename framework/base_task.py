from framework import Context
import argparse

from typing import Any

DATA_PATH = "data/"


class BaseTask(object):
    """
    Abstract task class.
    Please add your concrete code to concrete task class: `app/task.py`.
    """

    def __init__(self, context: Context) -> None:
        self.context = context
        self.args = self.get_arguments()

    def execute(self) -> Any:
        pass

    def get_arguments(self) -> argparse.Namespace:
        parser = argparse.ArgumentParser()
        self.set_arguments(parser)
        return parser.parse_args()

    def set_arguments(self, parser) -> None:
        pass
