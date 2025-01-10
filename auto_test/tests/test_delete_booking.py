import jsonschema
from playwright.sync_api import expect, APIRequestContext
from ..restful_booker.api import RestfulBookerAPI
from ..restful_booker.json_loder import load_schema

def test_delete_booking(api_request_context):
    data = {'firstname': 'Влад', 'lastname': 'Олегов', 'totalprice': 1435, 'depositpaid': True, 'bookingdates': {'checkin': '2013-02-23', 'checkout': '2014-10-23'}, 'additionalneeds': 'Beer'}

    restful_booker_api = RestfulBookerAPI(api_request_context=api_request_context)
    response_create_booking= restful_booker_api.create_booking(data)
    expect(response_create_booking).to_be_ok()

    response_create_booking_json = response_create_booking.json()
    expected_schema_create_booking = load_schema("auto_test/json/create_booking.json")
    jsonschema.validate(response_create_booking_json, expected_schema_create_booking)

    id = restful_booker_api.create_booking(data).json()["bookingid"]

    data_token = {"username": "admin", "password": "password123"}

    response_authorize = restful_booker_api.authorize(data_token)
    expect(response_authorize).to_be_ok()

    response_authorize_json = response_authorize.json()
    expected_schema_authorize = load_schema("auto_test/json/create_token.json")
    jsonschema.validate(response_authorize_json, expected_schema_authorize)

    token = response_authorize_json["token"]
     
    response_delete = restful_booker_api.delete_booking(id, token)
    expect(response_delete).to_be_ok()
    