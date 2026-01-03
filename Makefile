.PHONY: help install migrate test run docker-build docker-up docker-down clean

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install dependencies
	pip install -r requirements.txt

migrate: ## Run database migrations
	python manage.py migrate

collectstatic: ## Collect static files
	python manage.py collectstatic --noinput

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=core --cov=config --cov-report=html --cov-report=term

run: ## Run development server
	python manage.py runserver

superuser: ## Create a superuser
	python manage.py createsuperuser

docker-build: ## Build Docker image
	docker-compose build

docker-up: ## Start Docker containers
	docker-compose up

docker-down: ## Stop Docker containers
	docker-compose down

docker-shell: ## Open shell in Docker container
	docker-compose exec web bash

docker-test: ## Run tests in Docker
	docker-compose exec web pytest

clean: ## Clean up generated files
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -rf .coverage
