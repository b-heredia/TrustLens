import unittest
from analyzer import analyze_url


class TestURLAnalyzer(unittest.TestCase):

    def test_https_url(self):
        results = analyze_url("https://example.com")
        self.assertIn("This URL uses HTTPS.", results)

    def test_ip_address_detection(self):
        results = analyze_url("http://192.168.1.1")
        self.assertTrue(
            any(result.startswith(
                "Warning: This URL uses an IP address"
            ) for result in results)
        )

    def test_long_url_detection(self):
        url = "https://example.com/" + ("a" * 110)
        results = analyze_url(url)
        self.assertTrue(
            any(result.startswith(
                "Warning: This URL is unusually long."
            ) for result in results)
        )

    def test_username_information_detection(self):
        results = analyze_url("https://trusted.com@fake.com")
        self.assertTrue(
            any("username information" in result.lower() for result in results)
        )

    def test_url_shortener_detection(self):
        results = analyze_url("https://bit.ly/example")
        self.assertTrue(
            any("URL shortening service" in result for result in results)
        )

    def test_uncommon_domain_ending_detection(self):
        results = analyze_url("https://example.xyz")
        self.assertTrue(
            any("domain ending" in result for result in results)
        )


if __name__ == "__main__":
    unittest.main()