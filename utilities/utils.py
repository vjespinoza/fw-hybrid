import json

from config.constants import USER_AGENTS_FILE, WEB_CONFIG_FILE
from config.local_environment import LocalEnvironment


def extract_json_data(file: str):
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def get_user_agent(env: LocalEnvironment):
    data = extract_json_data(USER_AGENTS_FILE)
    return data[env.get_resolution()]


def get_screen_resolutions(env: LocalEnvironment, as_tuples: bool):
    data = extract_json_data(WEB_CONFIG_FILE)
    resolution = data["resolutions"][env.get_resolution()]
    if as_tuples:
        w, h = resolution.split("x")
        return int(w), int(h)
    else:
        return resolution
