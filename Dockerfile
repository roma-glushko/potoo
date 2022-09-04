FROM apache/airflow:2.3.4 as base

COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    rm ./requirements.txt