all: isort yapf flake8 mypy pytest

isort:
	isort -y -rc ./app

yapf:
	yapf -i -r app

flake8:
	flake8 app

mypy:
	mypy app

test:
	pytest
