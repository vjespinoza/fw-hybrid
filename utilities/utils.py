import json
import os
from typing import Any, Tuple

from dotenv import load_dotenv

from config.constants import BROWSER_RESOLUTIONS


def get_variable(var_name: str) -> str:
    load_dotenv()
    return str(os.getenv(var_name)).lower()


def extract_json_data(file: str) -> Any:
    f = open(file)
    data = json.load(f)
    f.close()
    return data


def browser_resolution(screen_size: str) -> Tuple[int, int, str]:
    data = extract_json_data(file=BROWSER_RESOLUTIONS)
    width = data[screen_size]['resolution'][0]
    height = data[screen_size]['resolution'][1]
    user_agent = data[screen_size]['user_agent']
    return width, height, user_agent


def capitalize_text(text: str) -> str:
    return text.title()
