all: test lint

test:
	BB_LOGLVL=WARNING $(PYTHON) coverage run --source brambox setup.py test -q

lint:
	$(PYTHON) pycodestyle --max-line-length=250 ./brambox/ && \
	$(PYTHON) pycodestyle --max-line-length=250 ./scripts/ && \
	$(PYTHON) pycodestyle --max-line-length=400 ./tests/

coverage:
	$(PYTHON) coverage report

docs:
	cd ./docs && make clean html

.PHONY: test lint coverage docs
