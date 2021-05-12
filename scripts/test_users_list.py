import pytest
import requests as req
import json, jsonpath


def test_users():

    url = "https://reqres.in/api/users?page=2"

    response = req.get(url)
    status_code = response.status_code

    json_response = json.loads(response.text)

    total_users = jsonpath.jsonpath(json_response, "total")
    total_page = jsonpath.jsonpath(json_response, "total_pages")

    assert status_code == 200, "HTTP Status Code should be 200"
    assert total_users[0] == 12, "Total users count is not right"
    assert total_page[0] == 2, "Total pages count is not right"
