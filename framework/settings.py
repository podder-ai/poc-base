import os
from typing import Optional


def get(key: str) -> Optional[str]:
    return os.environ.get(key)


# Shortcut variables for Framework.
PIPELINE_DATABASE_URL = get('PIPELINE_DATABASE_URL')
