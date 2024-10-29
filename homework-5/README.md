# Homework 5

[DataTalksClub/machine-learning-zoomcamp/cohorts/2024/05-deployment/homework.md](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/cohorts/2024/05-deployment/homework.md)

### Before solving tasks

Please install black

```bash
pip install black
```

And remember to format your code!

```bash
black .
```

### Question 1.

Install Pipenv:

```bash
pip install pipenv
```

Check the version of installed pipenv:

```bash
pipenv --version
```

Output:

```text
pipenv, version 2024.1.0
```

### Question 2.

With Pipenv install Scikit-Learn version 1.5.2

```bash
pipenv install scikit-learn==1.5.2
```

Then in [Pipfile.lock](Pipfile.lock) following data was found:

```text
    ...

        "scikit-learn": {
            "hashes": [
                "sha256:03b6158efa3faaf1feea3faa884c840ebd61b6484167c711548fce208ea09445",
    
    ...
```

### Models

Download `dv` and `model`:

```
PREFIX=https://raw.githubusercontent.com/DataTalksClub/machine-learning-zoomcamp/master/cohorts/2024/05-deployment/homework
wget $PREFIX/model1.bin
wget $PREFIX/dv.bin
```

### Question 3.

Launch subshell in pipenv virtual environment:

```bash
pipenv shell
```

Run in this shell [src/question3.py](src/question3.py) script:

```bash
python src/question3.py
```

Output:

```text
0.759
```

### Question 4.

With pipenv install Flask, gunicorn and requests

```bash
pipenv install Flask gunicorn requests
```

Open pipenv shell:

```bash
pipenv shell
```

Run gunicorn server with Flask app:

```bash
gunicorn --bind=localhost:5000 src.question4-server:app
```

Open pipenv shell in new terminal.

```bash
pipenv shell
```

Run in this shell [src/question4.py](src/question4.py) script:

```bash
python src/question4.py
```

Output:

```text
0.335
```

### Question 5.

Download the base image `svizor/zoomcamp-model:3.11.5-slim` with [docker pull](https://docs.docker.com/reference/cli/docker/image/pull/) command.

```bash
docker image pull svizor/zoomcamp-model:3.11.5-slim
```

Run `docker images` command:

```bash
docker images
```

Output:

```bash
REPOSITORY              TAG           IMAGE ID       CREATED      SIZE
svizor/zoomcamp-model   3.11.5-slim   975e7bdca086   2 days ago   130MB
```

### Question 6.

Build the Docker image from the [Dockerfile](Dockerfile)

```bash
docker build -t question6 .
```

Run docker container:

```bash
docker run -p 5000:5000 -d question6
```

Open pipenv shell:

```bash
pipenv shell
```

Run in this shell [src/question6.py](src/question6.py) script:

```bash
python src/question6.py
```

Output:

```text
0.757
```