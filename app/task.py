from framework.tasks import BaseTask
from framework.context import Context
from typing import Any

DATA_PATH = "data/"


class Task(BaseTask):
    """
    Concrete task class.
    """

    def __init__(self, context: Context) -> None:
        super().__init__(context)

    def execute(self) -> Any:
        """
        Concrete execute method.

        Notes
        -----
        1. Logging:
            You can output logs with `self.context.logger`.
            (e.g.) self.context.logger.debug("logging output")
        2. Command Line Arguments:
            You can access to arguments through `self.args` after set your arguments
            through `set_arguments` method.
            (e.g.) self.context.config.get('model_path')
        3. File Path:
            You can get absolute path to `data` directory by `self.context.file.get_data_path`.
            Please put your data or saved_models under `data` directory.
            Also your can use `self.context.file.get_data_path` to get absolute path to `tmp` directory.
            (e.g.) self.context.file.get_data_path('sample.csv')
        """
        self.context.logger.debug("logging output")

    def set_arguments(self) -> None:
        """
        Set your command line arguments if necessary.

        Notes
        -----
        Adding command line arguments.
        (e.g.) `self.context.config.set_argument('--model', dest="model_path", help='set model path')`
        """
