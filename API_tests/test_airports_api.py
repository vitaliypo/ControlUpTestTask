import pytest
from utils.api_client import AirportGapClient

@pytest.fixture
def api_client():
    return AirportGapClient()

def test_verify_airport_count(api_client):
    response = api_client.get_airports()
    assert len(response["data"]) == 30

def test_verify_specific_airports(api_client):
    response = api_client.get_airports()
    airport_names = [airport["attributes"]["name"] for airport in response["data"]]
    
    expected_airports = [
        "Akureyri Airport",
        "St. Anthony Airport",
        "CFB Bagotville"
    ]
    
    for airport in expected_airports:
        assert airport in airport_names

def test_verify_distance_between_airports(api_client):
    response = api_client.calculate_distance("KIX", "NRT")
    distance = float(response["data"]["attributes"]["kilometers"])
    assert distance > 400
