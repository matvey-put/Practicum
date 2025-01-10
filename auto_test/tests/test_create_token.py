import jsonschema
from playwright.sync_api import expect, APIRequestContext
from ..restful_booker.api import RestfulBookerAPI
from ..restful_booker.json_loder import load_schema


def test_create_token(api_request_context: APIRequestContext):
    data = {"username": "admin", "password": "password123"}

    restful_booker_api = RestfulBookerAPI(api_request_context=api_request_context)
    response = restful_booker_api.authorize(data)
    expect(response).to_be_ok()

    responce_json = response.json()
    expected_schema = load_schema("auto_test/json/create_token.json")
    jsonschema.validate(responce_json, expected_schema)