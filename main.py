from email_tools.send_gmail import send_gmail_email
from filters import filter_general, filter_remove_bad_roles, filter_security
from job_scraper.scrape_jobs import get_jobs
from utils.utils import (add_excel_sheet, delete_files, get_date,
                         jobs_to_excel, print_jobs_bullet_points)

# ----------------------------------
# Set Variables
# ----------------------------------
DEBUG = False
SEND_EMAIL = True
EMAIL_INFO = {
    "FILES": [],  # leave this FILES line empty
    "EMAIL_SUBJECT": "Cox Jobs",
    "SENDER_EMAIL": "x@domain.com",
    "EMAIL_TO": ["x@domain.com", "x@domain.com", "x@domain.com"],
    "MESSAGE_BODY": "Attached are the relevant jobs from the Cox job site: https://jobs.coxenterprises.com/",
    # This requires a google app password - your standard login password wont work (see readme)
    "SENDER_APP_PASSWORD": "X"
}

# ----------------------------------


if __name__ == "__main__":
    # Scrape Jobs
    if DEBUG:
        # Local - pulls less results for debugging
        site_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&business_unit=Cox%20Automotive&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
    else:
        # Local (25 mile radius around Atlanta - full-time, individual contributor)
        site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Atlanta%2C%20GA%2C%20USA&latitude=33.7489954&longitude=-84.3879824&radius=25&nationwide=US&statewide=GA"
    all_jobs = get_jobs(site_url)

    # Filter all jobs to create new data sets
    security_roles = filter_security(all_jobs)
    roles_without_bad_terms = filter_remove_bad_roles(all_jobs)
    general_filter_roles = filter_general(all_jobs)

    if SEND_EMAIL:
        file = "Jobs-" + get_date() + ".xlsx"
        EMAIL_INFO["FILES"].extend([file])
        # Generate main file with all jobs
        jobs_to_excel(all_jobs, file)
        # Add new sheets in the existing excel file for each filter
        add_excel_sheet(security_roles, file, "Security-Filter")
        add_excel_sheet(general_filter_roles, file, "General-Filter")
        add_excel_sheet(roles_without_bad_terms, file,
                        "Roles-Without-Bad-Terms")
        # Send the email
        send_gmail_email(EMAIL_INFO)
        # Delete the place files from the local machine
        delete_files(EMAIL_INFO["FILES"])
    else:
        print("ALL JOBS:")
        print(print_jobs_bullet_points(all_jobs))
