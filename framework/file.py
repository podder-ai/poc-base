import os


class File(object):
    """
    File utility class.
    """

    def __init__(self):
        self.root_path = self._get_root_path()

    def get_shared_path(self, path: str = '') -> str:
        """
        Returns absolute path to `shared` directory.
        """
        return os.path.abspath(os.path.join(self.root_path, 'shared', path))

    def get_data_path(self, path: str = '') -> str:
        """
        Returns absolute path to `shared/data` directory.
        """
        return os.path.abspath(os.path.join(self.get_shared_path(), 'data', path))

    def get_tmp_path(self, path: str = '') -> str:
        """
        Returns absolute path to `shared/tmp` directory.
        """
        # return os.path.abspath(self.root_path + self.TMP_DIR + path)
        return os.path.abspath(os.path.join(self.get_shared_path(), 'tmp', path))

    def _get_root_path(self) -> str:
        if not os.environ.get("POC_BASE_ROOT"):
            return ""
        return os.environ.get("POC_BASE_ROOT")
