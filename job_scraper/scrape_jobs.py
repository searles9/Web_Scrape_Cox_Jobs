# Scrape Jobs
import time

import chromedriver_binary
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_jobs(base_url):
    '''Web scrapes jobs from the cox enterprise job site

    Args:
        base_url (str): URL of page 1 of the cox job site search results

    Returns:
        list: list of job results [ [title, location, division, url], ... ]
    '''
    print("--------------------------------------------------")
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
            print(f"Collected {len(job_list)} results from page {page}")
            for each_job in job_list:
                job_title = each_job.find_elements_by_xpath(
                    ".//div[@class='jobTitle']")[0]
                job_location = each_job.find_elements_by_xpath(
                    ".//div[@class='parent location']")[0]
                job_location = job_location.text
                try:
                    remote_location = each_job.find_elements_by_xpath(
                        ".//div[@class='child locationtype']")[0]
                    job_location = f"({remote_location.text}) {job_location}"
                except:
                    pass
                job_division = each_job.find_element_by_xpath(
                    ".//li[@class='job-data business_unit']")
                job_url = each_job.find_element_by_xpath(
                    ".//div[@class='jobTitle']/a").get_attribute('href')
                job_info = [job_title.text, job_location,
                            job_division.text, job_url]
                job_details.append(job_info)
        else:
            print(f"***Gathered jobs from {(page - 1)} pages")
            break
        page += 1
    driver.quit()
    print("--------------------------------------------------")
    return job_details
