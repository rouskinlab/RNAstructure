VERSION := $(shell git describe --always --dirty --long)
PYPI_PASSWORD := $(shell cat ~/.pypi_pass.txt)

default: 
	python setup.py install

pytest:
	pytest test -v

init:
	pip install -r requirements.txt

push_to_pypi:
	rm -fr dist
	python3 -m build
	twine upload -r pypi dist/* --user yvesmartindestaillades --password $(PYPI_PASSWORD)
	rm -fr dist