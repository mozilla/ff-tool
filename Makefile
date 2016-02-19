HERE = $(shell pwd)
VENV = $(HERE)/venv
BIN = $(VENV)/bin
PYTHON = $(BIN)/python
PIP = $(BIN)/pip
INSTALL = $(PIP) install
SPHINX_BUILDDIR = docs/_build
INSTALL_STAMP = $(VENV)/.install.stamp


.PHONY: all build test clean pypi testpypi pypi-register testpypi-register

all:	build test

build: $(VENV)/COMPLETE
$(VENV)/COMPLETE: requirements.txt
	virtualenv --no-site-packages --python=`which python` \
	    --distribute $(VENV)
	$(INSTALL) -r requirements.txt
	$(PYTHON) setup.py develop
	touch $(VENV)/COMPLETE

test:
	$(INSTALL) -r requirements.txt
	tox

clean:
	rm -rf venv  *egg*  dist  ./docs/_build  .tox
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -type d -exec rm -fr {} \;


#---------------------------------------
# for dev branch only
#---------------------------------------

# Create dist, egg dirs, upload package to pypi
pypi:
	$(PYTHON) setup.py sdist upload -r pypi
	$(PYTHON) setup.py bdist_egg upload -r pypi

# Create dist, egg dirs, upload package to testpypi
testpypi:
	$(PYTHON) setup.py sdist upload -r testpypi
	$(PYTHON) setup.py bdist_egg upload -r testpypi

# Register this project to Python Package Index
pypi-register:
	$(PYTHON) setup.py register -r pypi

# Register this project to Test Python Package Index
testpypi-register:
	$(PYTHON) setup.py register -r testpypi
