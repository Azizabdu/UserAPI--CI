import requests
import pytest
from  test_base  import TestBase

# create a class for the endpoint
class TestRegister(TestBase):

    # positive test case as class method
    def test_view_user_by_id(self):
        endpoint = f'{self.base_url}/register'
        payload = {
            "email":"eve.holt@reqres.in"
    "password" "test"
}

        response = requests.get(endpoint,json=payload)
        data =response.json()

        print(data)
        assert response.status_code == 200
        assert 'id' in data
        assert 'token' in data
        assert type(data['token']) == str
        
    # negative test case
    def test_register_with_missing_pasword(self):
        endpoint = f'{self.base_url}/register'
        payload = { 
             "email":"eve.holt@reqres.in",
             "password": "test"
}
        
        response = requests.post(endpoint,json=payload)
        data = response.sjon()

        print(data)
        assert response.status_code == 400
        assert data ['error'] == 'Missing password'
        



    def test_delete_user(self):
        endpoint = f'{self.base_url}/users/10'

        response = requests.get(endpoint)
        assert response.status_code == 200
        

