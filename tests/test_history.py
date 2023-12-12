from dotenv import load_dotenv

load_dotenv()

import unittest
from app import app


class HistoryRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_history_route(self):
        self.client.get("/weather?city=São Paulo")

        response = self.client.get("/history")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, "application/json")

        data = response.json
        self.assertIsInstance(data, list)
        self.assertGreaterEqual(len(data), 1)


if __name__ == "__main__":
    unittest.main()
