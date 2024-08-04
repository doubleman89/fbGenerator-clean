import pytest
from collections import UserDict
from dataclasses import asdict

from generator.requests.network_type.create_network_type import CreateNetworkTypeRequestObject




wrong_network_type_dict ={
    "name" : "ok",
    "version" : "0.1",
    "comment" : "blablab",
    "tags" : {"",},
    "rows" : [],
    "common_data" : {"stat":[]},

}


correct_network_type_dict ={
    "name" : "ok",
    "version" : "0.1",
    "comment" : "blablab",
    "tags" : {"d":"sd"},
    "rows" : [],
    "common_data" : {"stat":UserDict({"d":"534"}), "temp":{"fsd":"sdsd"}},

}

@pytest.mark.parametrize("data", [wrong_network_type_dict])
def test_create_network_type_request_with_invalid_data(data):
    request = CreateNetworkTypeRequestObject.from_dict(data)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "tags"
    assert request.errors[0]["message"] == "Field tags has a wrong parameter type. It was declared as set, but it should be dict"
    assert request.errors[1]["parameter"] == "common data"
    assert request.errors[1]["message"] == "Field temp is required, but was not included as a parameter"
    assert request.errors[2]["parameter"] == "common data"
    assert request.errors[2]["message"] == "Field stat is not a dictionary"

    assert bool(request) is False

@pytest.mark.parametrize("data", [{}])
def test_create_network_type_request_with_empty_data(data):
    request = CreateNetworkTypeRequestObject.from_dict(data)
    keys = list(wrong_network_type_dict.keys())

    assert request.has_errors()
    for i in range(len(request.errors)):
        assert request.errors[i]["parameter"] == str(keys[i])
        assert request.errors[i]["message"] == f'Field {str(keys[i])} is required, but was not included as a parameter'

    assert bool(request) is False


@pytest.mark.parametrize("data", [correct_network_type_dict])
def test_create_network_type_request_with_correct_data(data):
    request = CreateNetworkTypeRequestObject.from_dict(data)

    assert vars(request) == data
    assert bool(request) is True

