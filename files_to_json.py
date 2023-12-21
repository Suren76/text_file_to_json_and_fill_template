import json
import os

from get_json import get_json_from_file
from os import listdir, path

from utils import remove_last_backslash_if_there_are, get_file_folder

class ConvertFilesToJsonException(Exception): pass
class InvalidPathException(ConvertFilesToJsonException): pass


def convert_files_to_json(path_to_files: str, to_save_file: str, path_to_output_directory: str, save_in_one_file: bool = True):
    _all_datas: dict = {}

    if not path.exists(path_to_files):
        raise InvalidPathException(f"File/Directory didn't exists or path is invalid! \n")

    if not path.exists(path_to_output_directory):
        os.mkdir(path_to_output_directory)
    if not save_in_one_file and not path.exists(f"{remove_last_backslash_if_there_are(path_to_output_directory)}/{get_file_folder(path_to_files)}"):
        os.mkdir(f"{remove_last_backslash_if_there_are(path_to_output_directory)}/{get_file_folder(path_to_files)}")

    for filename in listdir(path_to_files):
        if filename[-4:] == ".txt":
            data = get_json_from_file(filename=filename, path_to_file=path_to_files)

            if not save_in_one_file:
                with open(f"{remove_last_backslash_if_there_are(path_to_output_directory)}/{remove_last_backslash_if_there_are(get_file_folder(path_to_files))}/{filename[:-4]}.json", "w+") as file:
                    file.write(data)
            else:
                _all_datas[filename[:-4]] = json.loads(data)

        if save_in_one_file:
            with open(f"{remove_last_backslash_if_there_are(path_to_output_directory)}/{to_save_file}", "w+") as file:
                file.write(json.dumps(_all_datas))


if __name__ == "__main__":
    convert_files_to_json("resources/Script/", "", "", False)