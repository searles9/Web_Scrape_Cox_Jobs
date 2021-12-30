# MAIN FILE / Web Scrape Cox Jobs
import scrape_jobs
import utils
import send_gmail

# ----------------------------------
# Set Variables
# ----------------------------------
DEBUG = False
SEND_EMAIL = True
EMAIL_INFO = {
            "FILES": [], # leave this FILES line empty
            "EMAIL_SUBJECT": "Cox Jobs",
            "SENDER_EMAIL": "x@domain.com",
            "EMAIL_TO": ["x@domain.com","x@domain.com","x@domain.com"],
            "MESSAGE_BODY": "Attached are the relevant jobs from the Cox job site: https://jobs.coxenterprises.com/",
            "SENDER_APP_PASSWORD": "X" # This requires a google app password - your standard login password wont work (see readme)
        }

# ----------------------------------

def filter_security(all_jobs):
    good_terms = ["Security","Cyber"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    return utils.filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)

def filter_general(all_jobs):
    good_terms = ["Security","Solutions","Cloud","Cyber","Reliability","Architect","Systems","System","Infrastructure"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    return utils.filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)

if __name__ == "__main__":
    # Scrape Jobs
    if DEBUG:
        # Local - pulls less results for debugging
        test_local_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&business_unit=Cox%20Automotive&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_local_jobs = scrape_jobs.get_jobs(test_local_url)
        # Remote Jobs
        test_remote_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_remote_jobs = scrape_jobs.get_jobs(test_remote_url,remote_jobs=True)
    else:
        # Local (25 mile radius around Atlanta - full-time, individual contributor)
        local_site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Atlanta%2C%20GA%2C%20USA&latitude=33.7489954&longitude=-84.3879824&radius=25&nationwide=US&statewide=GA"
        all_local_jobs = scrape_jobs.get_jobs(local_site_url)
        # Remote Jobs (full-time, individual contributor))
        remote_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_remote_jobs = scrape_jobs.get_jobs(remote_url,remote_jobs=True)
    all_jobs = all_local_jobs + all_remote_jobs
    

    # Filter all jobs to create new data sets
    security_roles = filter_security(all_jobs)
    general_filter_roles = filter_general(all_jobs)

    if SEND_EMAIL:
        file = "Jobs.xlsx"
        EMAIL_INFO["FILES"].extend([file])
        # Generate main file with all jobs
        utils.jobs_to_excel(all_jobs,file)
        # Add new sheets in the existing excel file for each filter
        utils.add_excel_sheet(security_roles,file,"Security-Filter")
        utils.add_excel_sheet(general_filter_roles,file,"General-Filter")
        # Send the email
        send_gmail.send_gmail_email(EMAIL_INFO)
        # Delete the place files from the local machine 
        utils.delete_files(EMAIL_INFO["FILES"])
    else:
        print("ALL JOBS:")
        print(utils.print_jobs_bullet_points(all_jobs))