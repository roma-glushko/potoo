from airflow import DAG
from airflow.decorators import task

with DAG(
    "add_promo_user",
    tags=["twitter-growth"],
    params={
        "username": Param(5, type="integer", minimum=3),
    },
) as dag:
    ...