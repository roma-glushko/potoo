PROJECT_NAME?=potoo

.PHONY: help
help:
	@echo "\033[1;37m$(PROJECT_NAME)\033[0m :: Available Commands"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

k3d-start:  ## Start a new k3d cluster
	@k3d cluster create $(PROJECT_NAME) \
		--agents 2 \
		--registry-create registry:0.0.0.0:8008 \
		--k3s-node-label type=agent@agent:0,1 \
		--volume "$(PWD)/.data/:/data@agent:0,1"

k3d-stop:  ## Stop the k3d cluster
	@k3d cluster delete $(PROJECT_NAME)

tilt: ## Deploy and start your dev flow
	@tilt up

_guard-%:
	@#$(or ${$*}, $(error $* is not set))

.PHONY: airflow
airflow:  ## Open Airflow dashboard
	@open http://localhost:8080/

migration-create: _guard-MSG  ## Create a new Alembic migration
	@cd src/potoo && alembic revision --autogenerate -m ${MSG}

migration-exec:  ## Run all migrations
	@cd src/potoo && alembic upgrade head

image: ## Build the image
	@docker build . --tag hlushko/potoo