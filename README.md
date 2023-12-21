- build docker image \
**docker build -t image_with_entrypoint_list_and_test_python-slim --rm .**

- run docker  \
**docker run -it --name my_app_2 --rm --mount type=bind,source="$(pwd)"/,target=/home/app image_with_entrypoint_list_and_test_python-slim -d=resources/Script/examples -O=/home/app/from_docker_slim_python**


- convert docker image to .tar for sharing \
**docker save latestversion-1.0.0.tar latestversion:1.0.0**


- load docker from .tar \
**docker load --input latestversion-1.0.0.tar**

* new version
* [app.tar]()
* [app-1.1.0.tar]()
* [project_with_edits.zip](https://drive.google.com/file/d/1gO0wnvwJYVH-t2K752OAagevAZRW3HRW/view?usp=sharing)