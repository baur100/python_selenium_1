import requests
import json


class TestPets:
    base_url = "http://petstore.swagger.io/v2"

    def endpoint_order(self, id):
        return f"/store/order/{id}"

    def get_url(self, id):
        return TestPets.base_url + self.endpoint_order(id)

    # POST    POST     POST     POST     POST

    def test_post_place_an_order(self):
        body = {
            "id": 8,
            "petId": 92694,
            "quantity": 1,
            "shipDate": "",
            "status": "placed",
            "complete": True
        }

        b = json.dumps(body)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(self.base_url + "/store/order", headers=headers, data=b, )
        # print(response.status_code)

        assert response.status_code == 200
        json_response = json.loads(response.text)
        order_id = json_response["id"]
        order_pet_id = json_response["petId"]
        order_quantity = json_response["quantity"]
        order_status = json_response["status"]
        order_complete = json_response["complete"]

        assert order_id == 8
        assert order_pet_id == 92694
        assert order_quantity == 1
        assert order_status == "placed"
        assert order_complete == True

    # GET   GET     GET    GET    GET

    def test_get_order_by_id(self):
        response = requests.request("GET", self.get_url(8))
        assert response.status_code == 200

        json_response = json.loads(response.text)

        order_id = json_response["id"]
        pet_id = json_response["petId"]
        order_quantity = json_response["quantity"]
        order_status = json_response["status"]

        assert order_id == 8
        assert pet_id == 92694
        assert order_quantity == 1
        assert order_status == "placed"

    # DELETE     DELETE     DELETE     DELETE      DELETE

    def test_delete_order_by_id(self):
        response = requests.request("DELETE", self.get_url(8))

        assert response.status_code == 200

        response = requests.request("GET", self.get_url(8))
        assert response.status_code == 404

        json_response = json.loads(response.text)
        assert json_response["code"] == 1
        assert json_response["type"] == "error"
        assert json_response["message"] == "Order not found"
