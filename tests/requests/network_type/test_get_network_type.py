import pytest

from generator.requests.network_type.get_network_type import GetNetworkTypeRequestObject

wrong_network_type_dict ={
    "id" : "dsfsdfgdgdfg",
    "name" : "ok",
    "version" : 0.1,
}

correct_network_type_dict ={
    "id" : "dsfsdfgdgdfg",
    "name" : "ok",
    "version" : "0.1",
}


@pytest.mark.parametrize("data", [wrong_network_type_dict])
def test_create_network_type_request_with_invalid_data(data):
    request = GetNetworkTypeRequestObject.from_dict(data)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "version"
    assert request.errors[0]["message"] == f"Field {request.errors[0]['parameter']} has a wrong parameter type. It was declared as float, but it should be str"

    assert bool(request) is False

@pytest.mark.parametrize("data", [{}])
def test_create_network_type_request_with_empty_data(data):
    request = GetNetworkTypeRequestObject.from_dict(data)
    keys = list(wrong_network_type_dict.keys())

    assert request.has_errors()
    for i in range(len(request.errors)):
        assert request.errors[i]["parameter"] == str(keys[i])
        assert request.errors[i]["message"] == f'Field {str(keys[i])} is required, but was not included as a parameter'

    assert bool(request) is False


@pytest.mark.parametrize("data", [correct_network_type_dict])
def test_create_network_type_request_with_correct_data(data):
    request = GetNetworkTypeRequestObject.from_dict(data)

    assert vars(request) == data
    assert bool(request) is True

