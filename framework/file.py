import os


class File(object):
    """
    File utility class.
    """
    DATA_DIR = 'data' + os.path.sep

    def get_path(self, path) -> str:
        """
        Returns absolute path to `data` directory.
        """
        return os.path.abspath(self.DATA_DIR + path)
