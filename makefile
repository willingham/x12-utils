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
