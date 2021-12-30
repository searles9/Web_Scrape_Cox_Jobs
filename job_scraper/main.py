# MAIN FILE / Web Scrape Cox Jobs
import scrape_jobs
import utils
import send_gmail

DEBUG = False
SEND_EMAIL = True
EMAIL_INFO = {
            "FILES": [],
            "EMAIL_SUBJECT": "Cox Jobs",
            "SENDER_EMAIL": "x",
            "EMAIL_TO": ["x","x","x"],
            "MESSAGE_BODY": "Attached are the relevant jobs from the Cox job site: https://jobs.coxenterprises.com/",
            "SENDER_APP_PASSWORD": "x"
        }

if __name__ == "__main__":
    # Scrape Jobs
    if DEBUG: # Grabs less
        test_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&business_unit=Cox%20Automotive&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_jobs = scrape_jobs.get_jobs(test_url)
    else: # Gathers all jobs
        # Get all jobs close to Atlanta GA (25 mile radius / full-time / individual contributor)
        site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Atlanta%2C%20GA%2C%20USA&latitude=33.7489954&longitude=-84.3879824&radius=25&nationwide=US&statewide=GA"
        all_jobs = scrape_jobs.get_jobs(site_url)
 
    if SEND_EMAIL:
        # Create excel file with jobs
        filename = "All_Jobs.xlsx"
        EMAIL_INFO["FILES"].append(filename)
        utils.jobs_to_excel(all_jobs,filename)
        send_gmail.send_gmail_email(EMAIL_INFO)
        utils.delete_files(EMAIL_INFO["FILES"])
    else:
        print(utils.print_jobs_bullet_points(all_jobs))


