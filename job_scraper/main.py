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
            "SENDER_APP_PASSWORD": "X"
        }

# ----------------------------------

def filter_security_roles(all_jobs):
    good_terms = ["Security","Cyber"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    return utils.filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)

def general_filter_roles(all_jobs):
    good_terms = ["Security","Solutions","Cloud","Cyber","Reliability","Architect","Systems","System","Infrastructure"]
    bad_terms = ["Senior","Lead","Azure","Principal","Release","Sr","Software",
                 "Manager", "Financal","Finance","Payroll","HR","Marketing","SEO",
                 "Tax","Photojournalist","Executive","Sales","Buissness","Compensation","Recruiting",
                 "Litigation","Payable","Vehicle","Arbitrator","UX","Recruiter"]
    return utils.filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)

if __name__ == "__main__":
    # Scrape Jobs
    if DEBUG: # Grabs less
        test_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&business_unit=Cox%20Automotive&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_jobs = scrape_jobs.get_jobs(test_url)
    else: # Gathers all jobs
        # Get all jobs close to Atlanta GA (25 mile radius / full-time / individual contributor)
        site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Atlanta%2C%20GA%2C%20USA&latitude=33.7489954&longitude=-84.3879824&radius=25&nationwide=US&statewide=GA"
        all_jobs = scrape_jobs.get_jobs(site_url)
 
    # Filter for security roles
    security_jobs = filter_security_roles(all_jobs)
    # General filter to filter out bad roles
    general_filtered_roles = general_filter_roles(all_jobs)

    if SEND_EMAIL:
        # Add file names to create
        all_jobs_file = "All_Jobs.xlsx"
        security_jobs_file = "Security_Jobs.xlsx"
        filtered_jobs_file = "Filtered_Jobs.xlsx"
        EMAIL_INFO["FILES"].extend([all_jobs_file, security_jobs_file, filtered_jobs_file])
        # Create files
        utils.jobs_to_excel(all_jobs,all_jobs_file)
        utils.jobs_to_excel(security_jobs,security_jobs_file)
        utils.jobs_to_excel(general_filtered_roles,filtered_jobs_file)
        # Send email
        send_gmail.send_gmail_email(EMAIL_INFO)
        # Delete files from the local machine 
        utils.delete_files(EMAIL_INFO["FILES"])
    else:
        print(utils.print_jobs_bullet_points(all_jobs))


