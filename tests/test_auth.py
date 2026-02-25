import uuid
from pydantic import EmailStr

def test_register(client):

    email = "test_3@gmail.com"

    response = client.post("/auth/register", 
                           json={
                               "email": email,
                               "password" : "123456"
                           }
    )

    assert response.status_code == 200


def test_login(client):         # bina server run kare api endpoints ko access

    email = "test_3@gmail.com"

    response = client.post("/auth/login",      
                data={
                    "username" : email,
                    "password" : "123456"
                }
                )
    if response.status_code == 422:
        print(response.json())
    assert response.status_code == 200
    assert "access_token" in response.json()     # access token hai ya nahi 