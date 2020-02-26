import requests
import pytest
import json

class TestApiPets:

    base_url = "http://petstore.swagger.io/v2/"

    def get_pet_url(self, id):
        url = f"{self.base_url}pet/{id}"
        return url

    def json_data(self):
        filename = "pet.json"
        with open(filename) as file:
            return json.load(file)


    def test_post_pet(self):
        payload = json.dumps(self.json_data(), indent=4)
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.base_url + "pet", headers=headers, data=payload)
        res_dict = json.loads(response.text)

        assert response.status_code == 200
        assert res_dict["id"] == 99332222555
        assert res_dict["name"] == "Anfisa new new"


    def test_get_pet(self):
        response = requests.get(self.get_pet_url(99332222555))
        res_json = response.json()

        assert response.status_code == 200
        assert res_json["id"] == 99332222555
        assert res_json["category"]["name"] == "cats"
        assert res_json["name"] == "Anfisa new new"



    def test_del_pet(self):
        response = requests.delete(self.get_pet_url(99332222555))
        assert response.status_code == 200

        response = requests.get(self.get_pet_url(99332222555))
        assert response.status_code == 404

        json_response = json.loads(response.text)
        assert json_response["code"] == 1
        assert json_response["type"] == "error"
        assert json_response["message"] == "Pet not found"








