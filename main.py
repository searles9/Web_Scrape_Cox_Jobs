# MAIN FILE
# Web Scrape Cox Jobs
import scrape_jobs

if __name__ == "__main__":
    # Get all jobs close to Atlanta GA (site url needs to be updated)
    site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
    all_jobs = scrape_jobs.get_jobs(site_url)