.PHONY: help install test clean run dev

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make test     - Run tests"
	@echo "  make run      - Run the application"
	@echo "  make clean    - Clean temporary files"
	@echo "  make dev      - Install in development mode"

install:
	pip install -r requirements.txt

dev:
	pip install -e .
	pip install pytest black flake8

test:
	pytest TestUnitaire/ -v

run:
	python -m contact_manager.main

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -f contacts.json
