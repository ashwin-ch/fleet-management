# Choose the docker image  which needs to be used as baseline
FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "fleet_manager.py" ]

