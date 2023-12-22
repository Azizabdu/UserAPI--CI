import requests
import pytest
from test_basei import TestBase

# create a class for the endpoint
class TestUsers(TestBase):

    # positive test case as class method
    # @pytest.mark.smoke
    def test_view_user_by_id(self):
        endpoint = f'{self.base_url}/users/10'

        response = requests.get(endpoint)
        data =response.json()

        assert response.status_code == 200
        assert data ['data']['id'] == 100
        assert 'data' in data.keys()
        assert 'support' in data.keys()
        
    # negative test case
    def test_view_non_existent_user(self):
        endpoint = f'{self.base_url}/users/100'

        response = requests.get(endpoint)

        assert response.status_code == 204  



    def test_delete_user(self):
        endpoint = f'{self.base_url}/users/10'

        response = requests.get(endpoint)

        assert response.status_code == 200
        

