PYTHON=python
PIP=pip
SRC_TEST=tests

sort-imports:
	isort .

test:
	$(PYTHON) -m unittest discover -s $(SRC_TEST) -p "test_*.py" -v
