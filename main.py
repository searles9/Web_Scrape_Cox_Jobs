# MAIN FILE
# Web Scrape Cox Jobs
import scrape_jobs
import utils
debug = True

if __name__ == "__main__":
    if debug:
        # 26 jobs
        test_url = "https://jobs.coxenterprises.com/job-search-results/?keyword=security&business_unit=Cox%20Automotive&category[]=Information%20Technology&level=Individual%20Contributor&employment_type=Full-time&location=Norcross%2C%20GA%2C%20US&latitude=33.906&longitude=-84.184&radius=25"
        all_jobs = scrape_jobs.get_jobs(test_url)
    else:
        # Get all jobs close to Atlanta GA (25 mile radius / full-time / individual contributor)
        site_url = "https://jobs.coxenterprises.com/job-search-results/?level=Individual%20Contributor&employment_type=Full-time&location=Atlanta%2C%20GA%2C%20USA&latitude=33.7489954&longitude=-84.3879824&radius=25&nationwide=US&statewide=GA"
        all_jobs = scrape_jobs.get_jobs(site_url)

    print(utils.make_jobs_list_message(all_jobs))