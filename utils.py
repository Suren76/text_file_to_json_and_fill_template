from typing import Literal


def get_mode_state(name: Literal["single", "multiple"]) -> bool:
    return True if name == "multiple" else False


def remove_last_backslash_if_there_are(path: str) -> str:
    return path[:-1] if path[:-1] == '/' else path


def get_file_folder(path: str) -> str:
    return list(filter(str, path.split('/')))[-1]


def get_index_of_string_in_list(word: str, _list: list) -> int | None:
    for item in _list:
        if word in item:
            return _list.index(item)
    return None
