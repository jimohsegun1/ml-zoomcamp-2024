FROM python:3.9.7-slim

RUN pip install -U pip
RUN pip install pipenv

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["./Model/heart-model.bin", "./Model/"]
COPY ["./Script/predict.py", "./"]

EXPOSE 9797

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9797", "predict:app" ]
