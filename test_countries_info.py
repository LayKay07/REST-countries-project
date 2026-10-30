import unittest
from unittest.mock import Mock, patch

from countries_info import (
    get_country_info,
    get_african_countries,
    get_country_by_region,
)


def make_response(objects):
    """Create a mock API response using the expected response structure."""
    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        "data": {
            "objects": objects,
            "meta": {},
        }
    }
    return response


class TestCountryExplorer(unittest.TestCase):

    @patch("countries_info.requests.get")
    def test_get_country_info(self, mock_get):
        mock_get.return_value = make_response([
            {
                "names": {
                    "common": "Nigeria",
                    "official": "Federal Republic of Nigeria",
                },
                "capitals": [{"name": "Abuja"}],
                "region": "Africa",
                "population": 230000000,
                "area": {"kilometers": 923768},
                "currencies": [
                    {"name": "Naira", "symbol": "₦"}
                ],
                "languages": [{"name": "English"}],
            }
        ])

        result = get_country_info("nigeria")

        self.assertEqual(result["Country Name"], "Nigeria")
        self.assertEqual(result["Capital"], "Abuja")
        self.assertEqual(result["Region"], "Africa")
        self.assertEqual(result["Population"], 230000000)
        self.assertEqual(result["Languages"], ["English"])

    @patch("countries_info.requests.get")
    def test_country_not_found(self, mock_get):
        mock_get.return_value = make_response([])

        result = get_country_info("unknowncountry")

        self.assertEqual(result, {"Error": "Country not found"})

    @patch("countries_info.requests.get")
    def test_get_african_countries(self, mock_get):
        mock_get.return_value = make_response([
            {"names": {"common": "Nigeria"}},
            {"names": {"common": "Ghana"}},
        ])

        result = get_african_countries()

        self.assertEqual(result, ["Nigeria", "Ghana"])

    @patch("countries_info.requests.get")
    def test_get_country_by_region(self, mock_get):
        mock_get.return_value = make_response([
            {"names": {"common": "France"}},
            {"names": {"common": "Germany"}},
        ])

        result = get_country_by_region("Europe")

        self.assertEqual(result, ["France", "Germany"])


if __name__ == "__main__":
    unittest.main()
