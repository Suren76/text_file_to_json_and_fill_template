from typing import TypeAlias

from utils import remove_last_backslash_if_there_are

RawParsedDict: TypeAlias = dict


def parse_textfile_to_raw_dict(
        path_to_file,
        filename
) -> RawParsedDict:

    file = open(f"{remove_last_backslash_if_there_are(path_to_file)}/{filename}")

    raw_dictionary = {}

    index = 0
    for line in file.readlines():
        if len(line.strip()) == 0:
            continue

        _text_removed_newline = line[:-1:] if "\n" in line else line

        if ":" not in _text_removed_newline:
            if _text_removed_newline.strip() == "V-Ray":
                _text_removed_newline = "Vray"

            if raw_dictionary[index][-1][-1] == ":":
                raw_dictionary[index][-1] += " " + _text_removed_newline
                continue

            raw_dictionary[index][-1] += "+" + _text_removed_newline
            continue

        if ":" == _text_removed_newline[1:2]:
            index += 1
            raw_dictionary[index] = []

        _text_with_removed_index = _text_removed_newline[2:].strip() if _text_removed_newline[1:2] == ":" else _text_removed_newline

        raw_dictionary[index].append(_text_with_removed_index)

    file.close()

    return raw_dictionary
