project_name = "potoo"

docker_build(
  '%s/airflow:dev' % project_name,
  '.',
  dockerfile='Dockerfile',

  live_update=[
    sync('./airflow/dags', '/opt/airflow/dags'),
  ],
)

potoo_name = "potoo"
airflow_name = "airflow"
superflow_name = "superset"

k8s_yaml(helm('chart', name=airflow_name, namespace='airflow'))

k8s_resource('%s-postgresql' % potoo_name, port_forwards=5432, labels=["databases"])
k8s_resource('%s-redis' % airflow_name, port_forwards=6379, labels=["databases"])

k8s_resource('%s-scheduler' % airflow_name, labels=["airflow"])
k8s_resource('%s-run-airflow-migrations' % airflow_name, labels=["airflow"])
k8s_resource('%s-triggerer' % airflow_name, labels=["airflow"])
k8s_resource('%s-webserver' % airflow_name, port_forwards=8080, labels=["airflow"])
k8s_resource('%s-create-user' % airflow_name, resource_deps=['%s-postgresql' % airflow_name], labels=["airflow"])
k8s_resource('%s-cleanup' % airflow_name, labels=["airflow"])
k8s_resource('%s-worker' % airflow_name, labels=["airflow"])

k8s_resource(superflow_name, port_forwards=8088, labels=["superset"])
k8s_resource('%s-worker' % superflow_name, labels=["superset"])
k8s_resource('%s-init-db' % superflow_name, labels=["superset"])
