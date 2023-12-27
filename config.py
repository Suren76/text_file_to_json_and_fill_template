import json
from typing import Literal
import os

PATH_TO_PROJECT_FOLDR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_FILES_DIR = f"{PATH_TO_PROJECT_FOLDR}/resources/Script/"
TO_SAVE_FILE = f"full.json"
PATH_TO_OUTPUT_DIRECTORY = f"{PATH_TO_PROJECT_FOLDR}/output/"
MODE: Literal["single", "multiple"] = "multiple"

PATH_TO_CATEGORIES_LIST = f"{PATH_TO_PROJECT_FOLDR}/resources/categories list/json/converted_to_.json"

CATEGORIES_LIST = {
    str(key): str(value)
    for _item in json.loads(open(PATH_TO_CATEGORIES_LIST).read()).values()
    for key, value in _item.items()
}
