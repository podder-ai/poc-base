import os


class File(object):
    """
    File utility class.
    """
    DATA_DIR = 'data' + os.path.sep
    TMP_DIR = 'tmp' + os.path.sep

    def get_data_path(self, path: str = '') -> str:
        """
        Returns absolute path to `data` directory.
        """
        return os.path.abspath(self.DATA_DIR + path)

    def get_tmp_path(self, path: str = '') -> str:
        """
        Returns absolute path to `tmp` directory.
        """
        return os.path.abspath(self.TMP_DIR + path)
