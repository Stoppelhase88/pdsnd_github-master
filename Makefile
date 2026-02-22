.PHONY: venv test run

venv:
	python3 -m venv .venv && . .venv/bin/activate && pip install -U pip && pip install -r requirements.txt

test:
	pytest -q

run:
	python -m src.prompt_tools.prompt_metrics --file data/sample_prompt.txt
