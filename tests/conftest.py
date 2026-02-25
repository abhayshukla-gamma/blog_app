import pytest 
from fastapi.testclient import TestClient
from main import app

@pytest.fixture()                 # pytets framework ke andar aata hai reusable and constint testing env deta hai they manage setup of databases and handle cleanup 
def client():
    return TestClient(app)     # appp ko testing env me run jisme testing perform karenge 


