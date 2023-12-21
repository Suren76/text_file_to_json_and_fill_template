#!/usr/bin/env python

import argparse
# from config import PATH_TO_FILES_DIR, TO_SAVE_FILE, PATH_TO_OUTPUT_DIRECTORY, MODE
from script_config import *
from os import system


container_name = NAME_TO_RUN_IMAGE

mount_path = MOUNT_PATH
mount_path_in_image = MOUNT_PATH_IN_IMAGE

docker_image_name = DOCKER_IMAGE_NAME

path = PATH
to_save_file = TO_SAVE_FILE
path_to_output_directory = PATH_TO_OUTPUT_DIRECTORY
mode = MODE


parser = argparse.ArgumentParser()

parser.add_argument("-w", "--save-changes",
                    help=(
                        "(note) run with '-w true' or '--save-changes true' to work in default mode"
                        "run docker command to save them with default name configured in config file."
                        "if you want to specify the name then pass it through this param"
                    ))

parser.add_argument("-mp", "--mount-path", help="sets the path to mount in pc")
parser.add_argument("-mpi", "--mount-path-in-image", help="sets the path to mount in docker image")
parser.add_argument("-I", "--image-name", help="sets the name of image which script should run")

parser.add_argument("-d", "--directory", help="get path to directory and set as files folder")
parser.add_argument("-o", "--output-file", help="sets the name of file where to save if use single file mode")
parser.add_argument("-O", "--output-directory", help="sets the folder where files will be saved")
parser.add_argument("-m", "--mode", help="sets work mode. modes: single, multiple, edit")

args = parser.parse_args()


if args.save_changes:
    print(1)
    _save_image_name = docker_image_name
    if args.save_changes == "true":
        pass
    else:
        _save_image_name = args.save_changes

    system("".join([
        "docker commit",
        f" {container_name}"
        f" {_save_image_name}"
    ]))
    exit(0)
else:
    print("else", 0)


if args.mount_path:
    mount_path = args.mount_path
if args.mount_path_in_image:
    mount_path_in_image = args.mount_path_in_image
if args.image_name:
    docker_image_name = args.image_name

if args.directory:
    path = args.directory
if args.output_file:
    path_to_save_file = args.output_file
if args.output_directory:
    path_to_output_directory = args.output_directory
if args.mode:
    mode = args.mode

command = [
    "docker run ",
    " -it --rm ",
    f" --name TFTJ_run"
    f" -v $(pwd){str(mount_path)}:{str(mount_path_in_image)}",
    " -p 5000:5000",
    f" {docker_image_name}",
    # script params
    f" -m={mode}",
    f" -d={path}",
    f" -O={path_to_output_directory}"
    f" -o={to_save_file}"
]

# print(
#     "".join(["docker run ",
#     " -it --rm ",
#     f" -v $(pwd){str(mount_path)}:{str(mount_path_in_image)}",
#     " -p 5000:5000",
#     f" {docker_image_name}",
#     # script params
#     f" -m={mode}",
#     f" -d={path}",
#     f" -O={path_to_output_directory}"])
# )

system(
    "".join(command)
)
# docker run
# -it --rm
# -v $(pwd)"/docker_image_inside_mount":"/home/app"
# -p 5000:5000
# latest_app

# script params
# -m edit
# -d=resources/Script/examples
# -O=/home/app/from_docker_slim_python**
#
# convert_files_to_json(path, path_to_save_file, path_to_output_directory, True if mode == "multiple" else False)


