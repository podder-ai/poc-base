from typing import Any, List

from podder_task_base.context import Context
from podder_task_base.log import logger
from podder_task_base.tasks import BaseTask

DATA_PATH = "data/"


@logger.class_logger
class Task(BaseTask):
    """
    Concrete task class.
    """

    def __init__(self, context: Context) -> None:
        super().__init__(context)

    def execute(self, inputs: List[Any]) -> List[Any]:
        """
        Concrete execute method.

        Notes
        -----
        1. Logging:
            You can output logs with `self.logger`.
            (e.g.) self.logger.debug("logging output")
        2. Command Line Arguments:
            You can access to arguments through `self.context.config.get` after set your arguments
            through `set_arguments` method.
            (e.g.) self.context.config.get('model_path')
        3. File Path:
            You can get absolute path to `data` directory by `self.context.file.get_data_path`.
            Please put your data or saved_models under `data` directory.
            Also your can use `self.context.file.get_tmp_path` to get absolute path to `tmp` directory.
            (e.g.) self.context.file.get_tmp_path('sample.csv')
        """
        self.logger.debug("Start executing...")
        self.logger.debug("inputs: {}".format(inputs))

        # Add your code here

        outputs = inputs
        self.logger.debug("outputs: {}".format(outputs))
        self.logger.debug("Complete executing.")
        return outputs

    def set_arguments(self) -> None:
        """
        Set your command line arguments if necessary.

        Notes
        -----
        Adding command line arguments.
        (e.g.) `self.context.config.set_argument('--model', dest="model_path", help='set model path')`
        """
        # This "inputs" value will be passed to execute method as an argument
        # "inputs".
        self.context.config.set_argument(
            '--inputs',
            dest='inputs',
            help='inputs list',
            required=True,
            nargs='+')
