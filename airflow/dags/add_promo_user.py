from airflow import DAG
from airflow.models.param import Param

with DAG(
    "add_promo_user",
    tags=["twitter-growth"],
    params={
        "username": Param(type="string"),
    },
) as dag:
    ...