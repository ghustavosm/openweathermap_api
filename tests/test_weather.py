from dotenv import load_dotenv

load_dotenv()

import unittest
from app import app


class WeatherRouteTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_weather_success(self):
        response = self.client.get("/weather?city=Brasília")
        self.assertEqual(response.status_code, 200)

        data = response.json
        self.assertIn("city", data)
        self.assertIn("list", data)


if __name__ == "__main__":
    unittest.main()
