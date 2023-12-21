FROM python:3.11-slim
ADD . /project
RUN pip3 install -r /project/requirements.txt
ADD "docker_image_inside_mount/views.py" "/usr/local/lib/python3.11/site-packages/flaskcode/"

RUN #chmod +x /project/TFTJ
ENTRYPOINT ["python", "/project/app.py"]

#FROM python:3.8-slim
#RUN useradd --create-home --shell /bin/bash app_user
#WORKDIR /home/app_user
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt
#USER app_user
#COPY . .
#CMD ["bash"]