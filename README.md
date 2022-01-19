# Web_Scrape_Cox_Jobs
The Cox job site dynamically populates with jobs, however it only displays 10 jobs per page. This script can be used to easily pull and filter the jobs from the job site.

* Job site: https://jobs.coxenterprises.com/
***
# TOC
1. [Important Setup Info](https://github.com/searles9/Web_Scrape_Cox_Jobs#important-setup-info)
2. [Usage / Quick Code Overview](https://github.com/searles9/Web_Scrape_Cox_Jobs#usage--quick-code-overview)

***
# Important Setup Info
**Complete the setup steps below:** <br><br>
To use the web scraper you need to have chrome and the chrome driver binary installed. 
The versions installed need to match. 
### Install chrome
* Download chrome: https://www.google.com/chrome/
### Install the chrome driver binary
* Docs on installing the chrome driver binary: https://pypi.org/project/chromedriver-binary/
```
# Install 
pip install chromedriver-binary-auto

# Reinstall
pip install --upgrade --force-reinstall chromedriver-binary-auto
```
### Install the other dependencies
* install the dependencies in the requirements.txt file
```
pip install -r requirements.txt
```
***
### Quick usage
First update the ```main.py``` file as needed. If needed also update the ```filters.py``` file.
Execute the ```main.py``` file to run the scraper:
```
python main.py
```
Expected output (for email):
```
Collected 10 results from page 37
Collected 10 results from page 38
Collected 10 results from page 39
Collected 10 results from page 40
Collected 10 results from page 41
Collected 5 results from page 42
***Gathered jobs from 42 pages
--------------------------------------------------
***Generating excel document with jobs
***Excel document successfully generated
***Adding 'Security-Filter' sheet to the excel file
        ***The 'Security-Filter' sheet has been added to Jobs-2022-01-03.xlsx
***Adding 'General-Filter' sheet to the excel file
        ***The 'General-Filter' sheet has been added to Jobs-2022-01-03.xlsx
***Adding 'Roles-Without-Bad-Terms' sheet to the excel file
        ***The 'Roles-Without-Bad-Terms' sheet has been added to Jobs-2022-01-03.xlsx
***Sending email with jobs
***The email was successfully sent!
***Deleted temporary job file from the system: Jobs-2022-01-03.xlsx
```
