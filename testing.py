import unittest
from app import get_news, get_jobs

class TestApp(unittest.TestCase):

    def test_get_news(self):
        # Test for fetching news with default parameters
        news = get_news()
        self.assertIsNotNone(news)  # Check if news is not None
        self.assertLessEqual(len(news), 5)  # Check if the length of news is less than or equal to 5

        # Test for fetching news with custom parameters
        news = get_news(page=2, limit=10)
        self.assertIsNotNone(news)  # Check if news is not None
        self.assertLessEqual(len(news), 10)  # Check if the length of news is less than or equal to 10

    def test_get_jobs(self):
        # Test for fetching jobs with default parameters
        jobs = get_jobs()
        self.assertIsNotNone(jobs)  # Check if jobs is not None
        self.assertLessEqual(len(jobs), 5)  # Check if the length of jobs is less than or equal to 5

        # Test for fetching jobs with custom parameters
        jobs = get_jobs(page=2, limit=10)
        self.assertIsNotNone(jobs)  # Check if jobs is not None
        self.assertLessEqual(len(jobs), 10)  # Check if the length of jobs is less than or equal to 10


if __name__ == '__main__':
    unittest.main()