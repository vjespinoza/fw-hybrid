import json
import os
from typing import Any

from config.exceptions import MissingEnvironmentVariableError
from dotenv import load_dotenv

from config.constants import USER_AGENTS_FILE, WEB_CONFIG_FILE


def get_variable(var_name: str) -> str:
    load_dotenv()
    if os.getenv(var_name) is None:
        raise MissingEnvironmentVariableError(var_name)
    else:
        return str(os.getenv(var_name)).lower()


def extract_json_data(file: str) -> Any:
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def get_user_agent(resolution: str) -> str:
    data = extract_json_data(USER_AGENTS_FILE)
    return str(data[resolution])


def get_screen_resolutions(resolution: str, as_tuples: bool) -> str | tuple[int, ...]:
    data = extract_json_data(WEB_CONFIG_FILE)
    res = data["resolutions"][resolution]
    if as_tuples:
        w, h = res.split("x")
        return tuple((int(w), int(h)))
    else:
        return str(res)
