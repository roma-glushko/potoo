from airflow.models.param import Param

from airflow import DAG

with DAG(
    "add_promo_user",
    tags=["twitter-growth"],
    params={
        "username": Param(type="string"),
    },
) as dag:
    ...
