FROM apache/airflow:2.4.0-python3.10 as base

COPY ./airflow/dags/ ${AIRFLOW_HOME}/dags/

