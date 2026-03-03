MANAGER ?= uv
BUMP ?= minor

.PHONY: test t lint l format f format-check type check release-check pre-commit lock bump-patch bump-minor bump-major patch release major

test t:
	$(MANAGER) run pytest

lint l:
	$(MANAGER) run ruff check

format f:
	$(MANAGER) run ruff format

format-check:
	$(MANAGER) run ruff format --check

type:
	$(MANAGER) run mypy

check: lint type test

release-check: format-check check lock

pre-commit:
	$(MANAGER) run pre-commit run --all-files

lock:
	$(MANAGER) lock --check

bump-patch:
	$(MANAGER) run bump-my-version bump patch

bump-minor:
	$(MANAGER) run bump-my-version bump minor

bump-major:
	$(MANAGER) run bump-my-version bump major

patch:
	@$(MAKE) release BUMP=patch

major:
	@$(MAKE) release BUMP=major

release:
	@test "$(BUMP)" = "patch" || test "$(BUMP)" = "minor" || test "$(BUMP)" = "major" || (echo "BUMP must be one of: patch, minor, major" && exit 1)
	@git remote get-url origin >/dev/null 2>&1 || (echo "Remote 'origin' is not configured" && exit 1)
	@git diff --quiet && git diff --cached --quiet || (echo "Git working tree must be clean" && exit 1)
	@git fetch origin
	@git checkout develop
	@git pull --ff-only origin develop
	@git checkout main
	@git pull --ff-only origin main
	@git checkout develop
	@git merge --no-ff main
	@$(MAKE) release-check
	@$(MANAGER) run bump-my-version bump $(BUMP) --commit --tag
	@git push origin develop --follow-tags
	@git checkout main
	@git merge --no-ff develop
	@git push origin main
	@git push origin --tags
	@git checkout develop
