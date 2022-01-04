import unittest
#import main
#import scrape_jobs
#import send_gmail
import utils

job_list = [ 
            ["Security Engineer 2","Atlanta, GA", "Cox Automotive", "https://jobs.com" ],
            ["Vehicle Condition Inspector","Atlanta, GA", "Cox Automotive", "https://jobs.com" ],
            ["Sr Software Engineer","Atlanta, GA", "Cox Automotive", "https://jobs.com" ]
        ]

class TestStrings(unittest.TestCase):
    def test_contains_term(self):
        """
        Checks if any of the terms in the list exsit in the string
        """
        the_string = "Senior Developer"
        the_list = ["Senior Developer","Azure"]
        result = utils.contains_term(the_string,the_list)
        self.assertTrue(result)

    def test_contains_term_2(self):
        """
        Checks if any of the terms in the list exsit in the string
        """
        the_string = "Senior Developer"
        the_list = ["Senior","Azure"]
        result = utils.contains_term(the_string,the_list)
        self.assertTrue(result)

class CheckFilters(unittest.TestCase):
    """
    Filters the list down and removes items that contain a term in the bad terms list
    """
    def test_filter_bad_jobs(self):
        bad_terms = ["Vehicle","Software"]
        result = utils.filter_jobs_by_title(job_list,bad_terms=bad_terms)
        expected_result = [["Security Engineer 2","Atlanta, GA", "Cox Automotive", "https://jobs.com" ]]
        self.assertEqual(result, expected_result)

    def test_filter_good_jobs(self):
        """
        Filters the list down to only contain items that contain
         a term in the good terms list.
        """
        good_terms = ["Security"]
        result = utils.filter_jobs_by_title(job_list,good_terms=good_terms)
        expected_result = [["Security Engineer 2","Atlanta, GA", "Cox Automotive", "https://jobs.com" ]]
        self.assertEqual(result, expected_result)

    def test_filter_both(self):
        bad_terms = ["Vehicle"]
        good_terms = ["Security","Software"]
        result = utils.filter_jobs_by_title(job_list,bad_terms=bad_terms,good_terms=good_terms)
        expected_result = [
             ["Security Engineer 2","Atlanta, GA", "Cox Automotive", "https://jobs.com" ],
             ["Sr Software Engineer","Atlanta, GA", "Cox Automotive", "https://jobs.com" ]
        ]
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main() 