# Job Site Data Set Filters

from utils import filter_jobs_by_title


def filter_security(all_jobs):
    good_terms = ["Security", "Cyber"]
    bad_terms = ["Senior", "Lead", "Azure", "Principal", "Release", "Sr", "Software",
                 "Manager", "Financal", "Finance", "Payroll", "HR", "Marketing", "SEO",
                 "Tax", "Photojournalist", "Executive", "Sales", "Buissness", "Compensation", "Recruiting",
                 "Litigation", "Payable", "Vehicle", "Arbitrator", "UX", "Recruiter", "Driver", "Front End", "Social Media", "Investment", "Billing",
                 "Client Service Representative", "Rewards Analyst", "Media Strategist"]
    return filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)


def filter_general(all_jobs):
    good_terms = ["Security", "Solutions", "Cloud", "Cyber", "Reliability",
                  "Architect", "Systems", "System", "Infrastructure", "Devops"]
    bad_terms = ["Senior", "Lead", "Azure", "Principal", "Release", "Sr", "Software",
                 "Manager", "Financal", "Finance", "Payroll", "HR", "Marketing", "SEO",
                 "Tax", "Photojournalist", "Executive", "Sales", "Buissness", "Compensation", "Recruiting",
                 "Litigation", "Payable", "Vehicle", "Arbitrator", "UX", "Recruiter", "Driver", "Front End", "Social Media", "Investment", "Billing",
                 "Client Service Representative", "Rewards Analyst", "Media Strategist"]
    return filter_jobs_by_title(all_jobs, good_terms=good_terms, bad_terms=bad_terms)


def filter_remove_bad_roles(all_jobs):
    bad_terms = ["Senior", "Lead", "Azure", "Principal", "Release", "Sr", "Software",
                 "Manager", "Financal", "Finance", "Payroll", "HR", "Marketing", "SEO",
                 "Tax", "Photojournalist", "Executive", "Sales", "Buissness", "Compensation", "Recruiting",
                 "Litigation", "Payable", "Vehicle", "Arbitrator", "UX", "Recruiter", "Driver", "Front End", "Social Media", "Investment", "Billing",
                 "Client Service Representative", "Rewards Analyst", "Media Strategist"]
    return filter_jobs_by_title(all_jobs, bad_terms=bad_terms)
