PYTHON=python
PIP=pip
SRC_TEST=tests

sort-imports:
	isort .

test:
	$(PYTHON) -m unittest discover -s $(SRC_TEST) -p "test_*.py" -v
# --------------------------------------------------
pep-scraper:
	autopep8 job_scraper/scrape_jobs.py --in-place

pep-scraper-diff:
	autopep8 job_scraper/scrape_jobs.py --diff
# --------------------------------------------------
pep-utils:
	autopep8 utils/utils.py --in-place

pep-utils-diff:
	autopep8 utils/utils.py --diff
# --------------------------------------------------
pep-email:
	autopep8 email_tools/send_gmail.py --in-place

pep-email-diff:
	autopep8 email_tools/send_gmail.py --diff
# --------------------------------------------------
pep-main:
	autopep8 main.py --in-place

pep-main-diff:
	autopep8 main.py --diff
# --------------------------------------------------
pep-filters:
	autopep8 filters.py --in-place

pep-filters-diff:
	autopep8 filters.py --diff
# --------------------------------------------------