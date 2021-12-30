# Web_Scrape_Cox_Jobs
**I INTEND TO CLEAN UP THE CODE LATER, BUT ITS FUNCTIONAL** <br><br>
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
# Usage / Quick Code Overview
### Setup needed to run the scraper
Before you can run the scraper you need to update the values in the ```main.py``` file.
* update the ```EMAIL_INFO``` dictionary
    * the script requires that you send the email from a gmail account
    * google requires that you use an app password. here is info on setting up an app password for google: https://support.google.com/accounts/answer/185833?hl=en
* update the ```site_url``` variable. go to the cox job site, do a search and grab the url
### Quick usage
Execute the ```main.py``` file to run the scraper (you need all files in the job_scraper folder to run this).
```
python main.py
```
Expected output (for email):
```
Collected 10 results from page 1
Collected 10 results from page 2
Collected 6 results from page 3
***Gathered jobs from 3 pages
--------------------------------------------------
***Generating excel document with jobs
***Excel document successfully generated
***Sending email with jobs
***The email was successfully sent!
***Deleted temporary job file from the system: All_Jobs.xlsx
```
