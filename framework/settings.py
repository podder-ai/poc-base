import os
from typing import Optional


def get(key: str) -> Optional[str]:
  return os.environ.get(key)


 # Shortcut variables for Framework.
POC_DATABASE_URL = get('POC_DATABASE_URL')