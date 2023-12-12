from dotenv import load_dotenv

load_dotenv()

import unittest
from app import app
from app.utils.strings import WELCOME_MESSAGE


class HomeRouteTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(WELCOME_MESSAGE, response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
