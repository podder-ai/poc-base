from typing import Any

from podder_task_foundation import Context, Task as BaseTask


class Task(BaseTask):
    """
    Concrete task class.
    """

    def initialize(self, context: Context) -> None:
        pass

    def execute(self, inputs: Any) -> Any:
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
        self.context.logger.debug("Start executing...")
        self.context.logger.debug("inputs: {}".format(inputs))

        # Add your code here

        outputs = inputs
        self.context.logger.debug("outputs: {}".format(outputs))
        self.context.logger.debug("Complete executing.")
        return outputs
