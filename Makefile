# --------- Development commands ---------

format: # Format code and sort imports
	poetry run black pretty_match tests
	poetry run isort pretty_match tests

lint: # Run code quality tools
	# Check pep8 style
	poetry run flake8 pretty_match tests
	# Check imports order
	poetry run isort pretty_match tests --check-only
	# Check code security issues
	poetry run bandit -r pretty_match
	# Check security issues with installed packages
	poetry run safety check

# Prevent running a file with same name
.PHONY: test
test: # Run tests
	poetry run pytest tests


# --------- GitHub Actions CI ---------

# Prevent running a file with same name
.PHONY: test
ci.test: # Run ci tests
	poetry run pytest tests


ci.lint: # Run code quality tools inside ci
	# Check pep8 style
	poetry run flake8 pretty_match
	# Check imports order
	poetry run isort pretty_match --check-only
	# Check code security issues
	poetry run bandit -r pretty_match
	# Check security issues with installed packages
	poetry run safety check
