from app import app

def test_home_route():
    # customer
    client = app.test_client()
    
    #create GET a "/"
    response = client.get("/")
    
    # send respose for test 200 OK
    assert response.status_code == 200
    
    # check menssage
    assert b"Hello World" in response.data
