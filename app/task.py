from framework import BaseTask
from framework import Context

DATA_PATH = "data/"


class Task(BaseTask):
    """
    Concrete task class.
    """

    def __init__(self, context: Context) -> None:
        super().__init__(context)

    def execute(self) -> None:
        """
        Concrete execute method.

        Notes
        -----
        1. Logging:
            You can output logs with `self.context.logger`.
            (e.g.) self.context.logger.debug("logging output")
        2. Env var:
            You can access to environment variables with `self.context.config`.
            (e.g.) self.context.config.get("KEY")
        3. Command Line Arguments:
            You can access to arguments through `self.args` after set your arguments
            through `set_arguments` method.
            (e.g.) self.args.model_path
        4. File Path:
            You can get absolute path under `data` directory by `self.context.file.get_path`.
            Please put your files (data set or any necessary files) under `data` directory.
            (e.g.) self.context.file.get_path('sample.csv')
        """

    def set_arguments(self, parser) -> None:
        """
        Set your command line arguments if necessary.

        Notes
        -----
        Adding command line arguments.
        (e.g.) `parser.add_argument('--model', dest="model_path", help='set model path')`
        """
