install:
	pip install poetry
	poetry install

test:
	poetry run pytest

format:
	poetry run black x12_utils tests

lint:
	poetry run black --check x12_utils tests

typecheck:
	poetry run mypy x12_utils

clean:
	rm -rf dist

build:
	poetry build

publish:
	poetry publish
	
poetryversion:
	poetry version $(version) 
	
version: poetryversion
	$(eval NEW_VERS := $(shell cat pyproject.toml | grep "^version = \"*\"" | cut -d'"' -f2))
	sed -i "" "s/__version__ = .*/__version__ = \"$(NEW_VERS)\"/g" x12_utils/__init__.py
	
