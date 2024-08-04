import pytest
from unittest import mock

from generator.requests.network_type.create_network_type import CreateNetworkTypeRequestObject,CreateNetworkTypeInputDto
from generator.use_cases.network_type.create_network_type import create_network_type_use_case
from tests.requests.network_type.test_create_network_type import wrong_network_type_dict, correct_network_type_dict
from generator.responses.responses import ResponseTypes

def test_check_use_case_with_incorrect_data():
    repo = mock.Mock()
    
    request = CreateNetworkTypeRequestObject.from_dict(wrong_network_type_dict)
    response = create_network_type_use_case(request,repo)

    assert bool(response) is False
    assert response.value["type"] ==ResponseTypes.PARAMETERS_ERROR


def test_check_use_case_with_empty_data():
    repo = mock.Mock()
    
    request = CreateNetworkTypeRequestObject.from_dict({})
    response = create_network_type_use_case(request,repo)

    #prepare message
    parameter_key =  "parameter"
    message_key = "message"    
    message = "\n".join(
        [
            f"{err[parameter_key]}: {err[message_key]}" 
            for err in request.errors
        ]
    )
    
    assert bool(response) is False
    assert response.value =={
        "type":ResponseTypes.PARAMETERS_ERROR,
        "message": message,
    }
    


""" check the behaviour of the use case when the repository raises an exception
or when the request is badly formatted"""
def test_use_case_create_network_type_handles_generic_error():
    repo = mock.Mock()
    repo.create.side_effect = Exception("Just an error message")

    request = CreateNetworkTypeRequestObject.from_dict(correct_network_type_dict)
    response = create_network_type_use_case(request,repo)

    assert bool(response) is False
    # assert repo.create.assert_called_with(correct_network_type_dict)
    assert response.value =={
        "type":ResponseTypes.SYSTEM_ERROR,
        "message": "Exception: Just an error message"
    }

""" check the behaviour of the use case when the repository raises an exception
or when the request is badly formatted"""
def test_use_case_create_network_type_with_data():
    repo = mock.Mock()

    request = CreateNetworkTypeRequestObject.from_dict(correct_network_type_dict)
    response = create_network_type_use_case(request,repo)

    assert bool(response) is True
    repo.create.assert_called_with([CreateNetworkTypeInputDto(**correct_network_type_dict)])
    assert response.value == None

