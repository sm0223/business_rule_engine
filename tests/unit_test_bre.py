# test_app.py
import pytest
from unittest.mock import patch
from app import app

test_data = {
    "application": {
        "application_number": "101",
        "applicant": [
            {
                "name": "Shubham",
                "city": "Delhi",
                "dob": "1998-01-02",
                "salary": 1500
            },
            {
                "name": "Ayantika",
                "city": "Bangalore",
                "dob": "1999-01-02",
                "salary": 1500
            }
        ]
    },
    "result": {
        "rate": None,
        "charges": None,
        "reference": None
    }
}

response_data = {
    "application": {
        "applicant": [
            {
                "city": "Delhi",
                "dob": "Fri, 02 Jan 1998 00:00:00 GMT",
                "name": "Shubham",
                "salary": 1500.0
            },
            {
                "city": "Bangalore",
                "dob": "Sat, 02 Jan 1999 00:00:00 GMT",
                "name": "Ayantika",
                "salary": 1500.0
            }
        ],
        "application_number": "101"
    },
    "result": {
        "charges": 500.0,
        "rate": 0.15,
        "reference": "Success"
    }
}

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_call_bre01_success(client):
    with patch('repos.bre01.flow.Bre01Flow') as MockFlow:
        mock_instance = MockFlow.return_value
        mock_instance.execute.return_value = {"status": "ok"}

        response = client.post('/bre01', json=test_data)
        print(response.get_json())
        assert response.status_code == 200
        assert response.get_json() == response_data

def test_call_bre01_exception(client):
    with patch('repos.bre01.flow.Bre01Flow') as MockFlow:
        mock_instance = MockFlow.return_value
        mock_instance.execute.side_effect = Exception("fail")

        response = client.post('/bre01', json="string")
        assert response.status_code == 500
