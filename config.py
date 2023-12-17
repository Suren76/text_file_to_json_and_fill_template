import json
from typing import Literal

PATH_TO_FILES_DIR = "resources/Script/"
PATH_TO_SAVE_FILE = "full.json"
PATH_TO_OUTPUT_DIRECTORY = "output/"
MODE: Literal["single", "multiple"] = "multiple"

PATH_TO_CATEGORIES_LIST = "resources/categories list/json/converted_to_.json"

CATEGORIES_LIST = {
    str(key): str(value)
    for _item in json.loads(open(PATH_TO_CATEGORIES_LIST).read()).values()
    for key, value in _item.items()
}
