
env-init:
	@mkdir -p ./airflow/dags ./airflow/logs ./airflow/plugins
	@echo -e "AIRFLOW_UID=$(id -u)" > .env

airflow-run:
	@docker-compose up

airflow-dashboard:
	@open http://localhost:8080

flower-run:
	@docker-compose --profile flower up

flower-dashboard:
	@open http://localhost:5555

airflow-info:
	@docker-compose run airflow-worker airflow info