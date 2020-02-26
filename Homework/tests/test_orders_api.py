import requests
import pytest
import json

class TestApiOrders:

    base_url = "http://petstore.swagger.io/v2/"

    def get_order_url(self, id):
        url = f"{self.base_url}store/order/{id}"
        return url

    def json_data(self):
        filename = "order.json"
        with open(filename) as file:
            return json.load(file)


    def test_post_pet(self):
        payload = json.dumps(self.json_data(), indent=4)
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.base_url + "store/order", headers=headers, data=payload)
        res_dict = json.loads(response.text)

        assert response.status_code == 200
        assert res_dict["id"] == 111222333444555
        assert res_dict["quantity"] == 5
        assert res_dict["status"] == "placed"


    def test_get_order(self):
        response = requests.get(self.get_order_url(111222333444555))
        res_json = response.json()

        assert response.status_code == 200
        assert res_json["id"] == 111222333444555
        assert res_json["petId"] == 555333
        assert res_json["quantity"] == 5
        assert res_json["status"] == "placed"



    def test_del_order(self):
        response = requests.delete(self.get_order_url(111222333444555))
        assert response.status_code == 200

        response = requests.get(self.get_order_url(111222333444555))
        assert response.status_code == 404
