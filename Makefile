MANAGER ?= uv

.PHONY: test t lint l format f type check pre-commit lock

test t:
	$(MANAGER) run pytest

lint l:
	$(MANAGER) run ruff check

format f:
	$(MANAGER) run ruff format

type:
	$(MANAGER) run mypy

check: lint type test

pre-commit:
	$(MANAGER) run pre-commit run --all-files

lock:
	$(MANAGER) lock --check
