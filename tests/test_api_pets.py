import pytest
import requests
import json

from models.category import Category
from models.pet import Pet
from models.tag import Tag


class TestPets:
    base_url = "http://petstore.swagger.io/v2"

    def endpoint_pet(self, id):
        return f"/pet/{id}"

    def get_url(self, id):
        return TestPets.base_url + self.endpoint_pet(id)

    def test_get_pet_by_id(self):
        response = requests.request("GET", self.get_url(888999))
        assert response.status_code == 200

        json_response = json.loads(response.text)

        pet_name = json_response["name"]
        pet_id = json_response["id"]
        pet_category = json_response["category"]

        assert pet_name == "Apple Pie 2"
        assert pet_id == 888999
        assert pet_category["id"] == 2
        assert pet_category["name"] == "dogs"

    def test_post_create_a_pet(self):
        # body = {
        #     "id": 77777,
        #     "category": {
        #         "id": 0,
        #         "name": "string"
        #     },
        #     "name": "doggie",
        #     "photoUrls": [
        #         "string"
        #     ],
        #     "tags": [
        #         {
        #             "id": 0,
        #             "name": "string"
        #         }
        #     ],
        #     "status": "available"
        # }
        category = Category(2, "Dogs")
        tag = Tag(5, "Red")
        pet = Pet(888888, "avaliable", "Dasye", category.__dict__, ["string"], [tag.__dict__])
        body = json.dumps(pet.__dict__) #.replace('"', '\"')
        headers = {'Content-Type': 'application/json' }

        response = requests.post(self.base_url + "/pet", headers=headers, data=body)

        assert response.status_code == 200
        json_response = json.loads(response.text)
        pet_name = json_response["name"]
        pet_id = json_response["id"]

        assert pet_name == "Dasye"
        assert pet_id == 888888

