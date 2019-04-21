install:
	pip install poetry
	poetry install

test:
	poetry run pytest

format:
	black x12_utils tests

lint:
	black --check x12_utils tests
