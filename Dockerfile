FROM apache/airflow:2.4.0-python3.10 as base

COPY ./airflow/dags/ ${AIRFLOW_HOME}/dags/

RUN pip install --no-cache-dir -U pip poetry==1.2.2

COPY pyproject.toml poetry.lock ./
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ARG POTOO_HOME=/opt/airflow/potoo

RUN mkdir $POTOO_HOME
ENV PYTHONPATH="$PYTHONPATH:$POTOO_HOME"
WORKDIR $POTOO_HOME

COPY /src/ $POTOO_HOME