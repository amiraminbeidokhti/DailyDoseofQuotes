PYTHON=python3
MAIN_SCRIPT=main.py

all: dependencies run

dependencies:
	@echo "Installing dependencies"
	$(PYTHON) -m pip install -r requirements.txt

run:
	@echo "Running the script"
	$(PYTHON) $(MAIN_SCRIPT)