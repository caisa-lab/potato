FROM python:3.11-slim-bookworm

WORKDIR /app


COPY ./project-hub /app/project-hub
COPY ./potato /app/potato
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install -U pip

RUN pip install -r requirements.txt

EXPOSE 8080

CMD exec python app/potato/flask_server.py start app/project-hub/spot_yaml_generation/configs/task_config.yaml -p 8080