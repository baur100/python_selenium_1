import requests


def endpoint_pet(id):
    return f"/pet/{id}"

base_url= "http://petstore.swagger.io/v2"

response = requests.request("GET",base_url+endpoint_pet(888999))


