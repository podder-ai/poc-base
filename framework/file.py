import os


class File(object):
    """
    File utility class.
    """
    DATA_DIR = 'data' + os.path.sep
    TMP_DIR = 'tmp' + os.path.sep

    def __init__(self):
        self.root_path = self._get_root_path()

    def get_data_path(self, path: str = '') -> str:
        """
        Returns absolute path to `data` directory.
        """
        return os.path.abspath(self.root_path + self.DATA_DIR + path)

    def get_tmp_path(self, path: str = '') -> str:
        """
        Returns absolute path to `tmp` directory.
        """
        return os.path.abspath(self.root_path + self.TMP_DIR + path)

    def _get_root_path(self) -> str:
        if not os.environ.get("POC_BASE_ROOT"):
            return ""
        root_path = os.environ.get("POC_BASE_ROOT")
        if not root_path.endswith('/'):
            root_path += '/'
        return root_path
