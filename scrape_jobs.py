# Scrape Jobs
from selenium import webdriver
import chromedriver_binary
import time

def get_jobs(base_url):
    """
    returns job_details: list of lists
    job_details = [ [title, location, division, url], ... ]
    """
    job_details = []
    page_still_valid = True
    page = 1
    driver = webdriver.Chrome()
    while page_still_valid:
        search_query = str(base_url) + "&pg=" + str(page)
        driver.get(search_query)
        time.sleep(5)
        job_list = driver.find_elements_by_class_name('job-innerwrap')
        if len(job_list) > 0:
            print(f"Collected {len(job_list)} results from page {str(page)}")
            for each_job in job_list:
            # Getting job info
                job_title = each_job.find_elements_by_xpath(".//div[@class='jobTitle']")[0]
                job_location = each_job.find_elements_by_xpath(".//div[@class='parent location']")[0]
                job_division = each_job.find_element_by_xpath(".//li[@class='job-data business_unit']")
                job_url = each_job.find_element_by_xpath(".//div[@class='jobTitle']/a").get_attribute('href')
                # Saving job info 
                job_info = [job_title.text, job_location.text, job_division.text, job_url]
                # Saving into job_details
                job_details.append(job_info)
        else: 
            print(f"***Gathered jobs from {(page - 1)} pages")
            break
        page += 1
    driver.quit()
    return job_details

