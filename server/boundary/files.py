import json
from pathlib import Path

from server.boundary import log


@log.try_except(message="JSON file not read", default={})
def get_json(path: Path) -> dict:
    with open(path, 'r') as fp:
        return json.load(fp)
