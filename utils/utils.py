# Functions to help filter and view the job data
import os
from datetime import date

import openpyxl
import pandas as pd
from tabulate import tabulate


def print_jobs_in_grid(jobs):
    '''Prints the inputed jobs to the cli in a grid format.

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]
    '''
    table = jobs
    headers = ["Title", "Location", "Division", "URL"]
    print(tabulate(table, headers, tablefmt="grid"))


def print_jobs_bullet_points(jobs):
    '''Prints the inputed jobs to the cli in a bullet point format

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]
    '''
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
    '''Takes the inputed jobs and returns them in a string bullet point format.

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]

    Returns:
        str: treturns the jobs in a bullet point string forma
    '''
    jobs_message = ""
    for job in jobs:
        jobs_message += f"* TITLE: {job[0]}\n"
        jobs_message += f"* LOCATION: {job[1]}\n"
        jobs_message += f"* DIVISION: {job[2]}\n"
        jobs_message += f"* URL: {job[3]}\n"
        jobs_message += "--------------------------------------------------\n"
    return jobs_message


def jobs_to_excel(jobs, filename):
    '''[summary]

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]
        filename (str): name of the excel file (with extension) that
                     you want to create
    '''
    print("***Generating excel document with jobs")
    df = pd.DataFrame(jobs)
    df.columns = ['Title', 'Location', 'Division', 'URL']
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Jobs', index=False)
    writer.save()
    print("***Excel document successfully generated")


def add_excel_sheet(jobs, file, sheetname):
    '''Adds an excel sheet contaning jobs to an existing excel file.

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]
        file (str): name of the excel file that you want to add a sheet to
        sheetname (str): name for new excel sheet
    '''
    print(f"***Adding '{sheetname}' sheet to the excel file")
    df = pd.DataFrame(jobs)
    df.columns = ['Title', 'Location', 'Division', 'URL']
    with pd.ExcelWriter(file, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=sheetname, index=False)
    print(f"\t***The '{sheetname}' sheet has been added to {file}")


def delete_files(files):
    '''Deletes file/files from the loca system

    Args:
        files (list): list of filenames
    '''
    for x in files:
        os.remove(x)
        print(f"***Deleted temporary job file from the system: {x}")


def contains_term(the_string, the_list):
    '''Checks if any of the terms in the list exist in the string.

    Args:
        the_string (str): string to check
        the_list (list): list of terms

    Returns:
        bool: If the string contains any of the items in the list return True
    '''
    for item in the_list:
        if item.upper() in the_string.upper():  # if the term is in the list
            return True
    return False


def filter_jobs_by_title(jobs, good_terms=[], bad_terms=[],):
    '''Filters job data set down.

    Args:
        jobs (list): List of lists containing jobs 
                     ["Title", "Location", "Division", "URL"]
        good_terms (list, optional): terms that the job title should contain. Defaults to [].
        bad_terms (list, optional): terms that the job title should not contain. Defaults to [].

    Returns:
        list: returns a new data set only containing the filtered jobs
    '''
    job_list = jobs
    # Filter once to drop items that contain bad terms
    if len(bad_terms) > 0:
        job_list = [job for job in job_list if not contains_term(
            job[0], bad_terms)]
    # Filter again to only include items that are in the good terms list
    if len(good_terms) > 0:
        job_list = [job for job in job_list if contains_term(
            job[0], good_terms)]
    return job_list


def get_date():
    '''Returns todays date as a string.

    Returns:
        str: todays date
    '''
    return str(date.today())
