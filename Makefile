PYTHON=python3
MAIN_SCRIPT=main.py

all: dependencies run

dependencies:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) $(MAIN_SCRIPT)