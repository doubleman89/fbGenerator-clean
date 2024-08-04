import pytest

from generator.requests.network_type.load_network_type import LoadNetworkTypeRequestObject




wrong_network_type_dict ={
    "name" : "ok",
    "version" : "0.1",
    "comment" : "blablab",
    "tags" : {""},
    "rows" : [],
    "common_data" : {"stat":[]},

}

wrong_network_type_dict2 ={
    "name" : "ok",
    "version" : "0.1",
    "comment" : "blablab",
    "tags" : {""},
    "rows" : [],
    "common_data" : {"srs":[]},

}


@pytest.mark.parametrize("data", [wrong_network_type_dict,{}])
def test_load_network_type_request_with_invalid_data(data):
    request = LoadNetworkTypeRequestObject.from_dict(data)

    print (request.errors)

    assert request.has_errors()
    assert request.errors[0]["parameter"] == "tags"
    assert request.errors[0]["message"] == "'This field has a wrong parameter type. It was declared as set, but it should be dict"
    assert request.errors[1]["parameter"] == "common data"
    assert request.errors[1]["message"] == "'Field temp is required, but was not included as a parameter"

    
    assert bool(request is False)



