import unittest
from app import app


class TestTrustLensApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_homepage_loads(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_valid_url_submission(self):
        response = self.client.post(
            "/",
            data={"url": "https://example.com"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"No predefined warning indicators detected.",
            response.data
        )

    def test_suspicious_url_submission(self):
        response = self.client.post(
            "/",
            data={"url": "http://192.168.1.1"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"2 warning indicators detected", response.data)

    def test_invalid_url_submission(self):
        response = self.client.post(
            "/",
            data={"url": "not-a-valid-url"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a valid URL",
            response.data
        )

    def test_empty_url_submission(self):
        response = self.client.post(
            "/",
            data={"url": ""}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a valid URL",
            response.data
        )

    def test_malformed_url_submission(self):
        response = self.client.post(
            "/",
            data={"url": "http://[invalid]"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a valid URL",
            response.data
        )

    def test_url_with_spaces(self):
        response = self.client.post(
            "/",
            data={"url": "https://example .com"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Please enter a valid URL",
            response.data
        )


if __name__ == "__main__":
    unittest.main()