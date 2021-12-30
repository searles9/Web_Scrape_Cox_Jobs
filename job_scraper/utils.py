# Functions to help filter and view the job data
from tabulate import tabulate
import pandas as pd
import os

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

def delete_files(files):
    for x in files:
        os.remove(x) 
        print(f"***Deleted temporary job file from the system: {x}")