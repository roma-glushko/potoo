project_name = "potoo"

docker_build(
  '%s/airflow:dev' % project_name,
  '.',
  dockerfile='docker/airflow.Dockerfile',

  live_update=[
    sync('./airflow/dags', '/opt/airflow/dags'),
  ],
)

airflow_name = "airflow"

k8s_yaml(helm('chart', name=airflow_name, namespace='airflow'))

k8s_resource('%s-scheduler' % airflow_name, labels=["airflow"])
k8s_resource('%s-run-airflow-migrations' % airflow_name, labels=["airflow"])
k8s_resource('%s-triggerer' % airflow_name, labels=["airflow"])
k8s_resource('%s-webserver' % airflow_name, port_forwards=8080, labels=["airflow"])
k8s_resource('%s-create-user' % airflow_name, resource_deps=['%s-postgresql' % airflow_name], labels=["airflow"])
k8s_resource('%s-postgresql' % airflow_name, labels=["airflow"])
k8s_resource('%s-cleanup' % airflow_name, labels=["airflow"])
