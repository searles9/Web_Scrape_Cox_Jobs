# Functions to help filter and view the job data
from tabulate import tabulate
import pandas as pd
import os
import openpyxl

def print_jobs_in_grid(jobs):
    """Prints jobs with a grid format

    Paramaters
    jobs: list of lists containing jobs
    """
    table = jobs
    headers = ["Title", "Location", "Division", "URL"]
    print(tabulate(table, headers, tablefmt="grid"))

def print_jobs_bullet_points(jobs):
    """Prints jobs in a simple bullet point format

    Paramaters
    jobs: list of lists containing jobs
    """
    for job in jobs:
        title = job[0]
        location = job[1]
        division = job[2]
        url = job[3]
        print(f"* TITLE: {title}")
        print(f"* LOCATION: {location}")
        print(f"* DIVISION: {division}")
        print(f"* URL: {url}")
        print("--------------------------------------------------")

def make_jobs_list_message(jobs):
    """
    Takes a list of jobs and returns them in a string
    """
    jobs_message = ""
    for job in jobs:
        jobs_message += f"* TITLE: {job[0]}\n"
        jobs_message += f"* LOCATION: {job[1]}\n"
        jobs_message += f"* DIVISION: {job[2]}\n"
        jobs_message += f"* URL: {job[3]}\n"
        jobs_message += "--------------------------------------------------\n"
    return jobs_message

def jobs_to_excel(jobs,filename):
    print("***Generating excel document with jobs")
    df = pd.DataFrame(jobs)
    df.columns = ['Title', 'Location', 'Division', 'URL']
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Jobs', index=False)
    writer.save()
    print("***Excel document successfully generated")

def add_excel_sheet(jobs,file,sheetname):
    print(f"***Adding {sheetname} sheet to the excel file")
    df = pd.DataFrame(jobs)
    df.columns = ['Title', 'Location', 'Division', 'URL']
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:  
        df.to_excel(writer, sheet_name=sheetname , index=False)
    print(f"***The sheet has been added to {file}")

def delete_files(files):
    for x in files:
        os.remove(x) 
        print(f"***Deleted temporary job file from the system: {x}")

def contains_substring(sub_string, the_string,):
    """Checks if sub_string exists in the_string and returns True if it does

    sub_string: str
    the_string: str
    """
    the_string = the_string.upper().split(" ")
    sub_string = sub_string.upper()
    if sub_string in the_string:
        return True
    return False

def contains_term(the_string, the_list):
    """Checks if the_string exists in the_list
    
    """
    for item in the_list:
        if contains_substring(item, the_string): # if the term is in the list
            return True
    return False

def filter_jobs_by_title(jobs, good_terms=[], bad_terms=[]):
    job_list = jobs
    # Filter once to drop items that contain bad terms
    if len(bad_terms) > 0:
        job_list = [job for job in job_list if not contains_term(job[0],bad_terms)]
    # Filter again to only include items that are in the good terms list
    if len(good_terms) > 0:
        job_list = [job for job in job_list if contains_term(job[0],good_terms)]
    return job_list