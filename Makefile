VERSION := $(shell git describe --always --dirty --long)
PYPI_TOKEN := $(shell cat ~/.pypi_token.txt)

default: 
	python setup.py install

test:
	pytest test.py -v

init:
	pip install -r requirements.txt

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/* --user __token__ --password $(PYPI_TOKEN)
	rm -fr dist