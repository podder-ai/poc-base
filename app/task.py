from typing import Any

from podder_task_foundation import Context, Task as BaseTask


class Task(BaseTask):
    """
    Concrete task class.
    """

    def initialize(self, context: Context) -> None:
        context.logger.debug("Start Initializing...")

    def execute(self, inputs: Any, context: Context) -> Any:
        """
        Concrete execute method.
        Notes
        -----
        1. Logging:
            You can output logs with `self.logger`.
            (e.g.) self.context.logger.debug("logging output")
        2. File Path:
            You can get absolute path to `data` directory by `self.context.file.get_data_path`.
            Please put your data or saved_models under `data` directory.
            Also your can use `self.context.file.get_tmp_path` to get absolute path to `tmp` directory.
            (e.g.) self.context.file.get_tmp_path('sample.csv')
        """
        context.logger.debug("Start executing...")
        context.logger.debug("inputs: {}".format(inputs))

        # Add your code here
        print("ABC")
        outputs = inputs
        context.logger.debug("outputs: {}".format(outputs))
        context.logger.debug("Complete executing.")
        return outputs
