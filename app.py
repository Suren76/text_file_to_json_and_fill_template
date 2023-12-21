#!/home/suren/.cache/pypoetry/virtualenvs/slack-bot-e3O-PR5L-py3.11/bin/python3.11

import argparse

from config import PATH_TO_FILES_DIR, TO_SAVE_FILE, PATH_TO_OUTPUT_DIRECTORY, MODE, PATH_TO_PROJECT_FOLDR
from files_to_json import convert_files_to_json
import os

from utils import remove_last_backslash_if_there_are

path = PATH_TO_FILES_DIR
to_save_file = TO_SAVE_FILE
path_to_output_directory = PATH_TO_OUTPUT_DIRECTORY
mode = MODE

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--directory", help="get path to directory and set as files folder")
parser.add_argument("-o", "--output-file", help="sets the name of file where to save if use single file mode")
parser.add_argument("-O", "--output-directory", help="sets the folder where files will be saved")
parser.add_argument("-m", "--mode", help="sets work mode. modes: single, multiple")

args = parser.parse_args()

# if args.shell:
#     while True:
#         pass


if args.mode:
    mode = args.mode
    if mode == "edit":
        os.system(f"python {remove_last_backslash_if_there_are(PATH_TO_PROJECT_FOLDR)}/online_editor.py")
if args.directory:
    path = args.directory
if args.output_file:
    to_save_file = args.output_file
if args.output_directory:
    path_to_output_directory = args.output_directory


convert_files_to_json(path, to_save_file, path_to_output_directory, True if mode == "multiple" else False)

