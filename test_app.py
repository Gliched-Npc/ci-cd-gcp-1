"""testing for fastapi service """

from fastapi.testclient import TestClient
from main import app

#creating a test client instance for the FastAPI application.
client=TestClient(app)

def test():
    """
    The `test` function sends a prediction request with specified features to a FastAPI service and
    asserts the response status code and presence of a "class_name" key in the response data.
    """
    resp=client.post('/predict',json={'features':[5.1,4.2,3.8,0.2]})
    assert resp.status_code==200

    data=resp.json()
    assert "class_name" in data