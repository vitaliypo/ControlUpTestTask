import requests

from config.test_configuration import TestConfig

class AirportGapClient:
    """API Client for Airport Gap"""
    def __init__(self):
        self.base_url = TestConfig.AIRPORT_GAP_BASE_URL

    def get_airports(self) -> dict:
        """
        Fetches the list of airports from the API.

        :return: A dictionary containing a list of airports and their details
        :rtype: dict
        """
        response = requests.get(f"{self.base_url}/airports")
        return response.json()

    def calculate_distance(self, from_airport: str, to_airport: str) -> dict:
        """
        Calculates the distance between two specified airports by sending a POST request
        to an external service.

        :param from_airport: IATA code of the departure airport
        :type from_airport: str
        :param to_airport: IATA code of the destination airport
        :type to_airport: str
        :return: A dictionary containing the calculated distance between the two airports
        :rtype: dict
        """
        payload = {
            "from": from_airport,
            "to": to_airport
        }
        response = requests.post(f"{self.base_url}/airports/distance", json=payload)
        return response.json()
