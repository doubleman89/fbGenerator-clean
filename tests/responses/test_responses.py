from generator.responses.responses import ResponseSuccess, ResponseFailure, ResponseTypes, build_response_from_invalid_request




SUCCESS_VALUE = {"key":["value1","value2"]}
GENERIC_RESPONSE_TYPE = "Response"
GENERIS_RESPONSE_MESSAGE = "This is a response"


""" first check if responses have a boolean value"""
def test_response_success_is_true():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert bool(response) is True


def test_response_success_is_false():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE,GENERIS_RESPONSE_MESSAGE)
    
    assert bool(response) is False
    
""" then test structure of responses, checking type an value
ResponseFailure objects should also have a message attribute 
"""

def test_response_success_has_type_and_value():
    response = ResponseSuccess(SUCCESS_VALUE)

    assert response.type == ResponseTypes.SUCCESS
    assert response.value == SUCCESS_VALUE


def test_response_failure_has_type_and_message():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE,GENERIS_RESPONSE_MESSAGE)    

    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == GENERIS_RESPONSE_MESSAGE
    assert response.value == {
        "type" : GENERIC_RESPONSE_TYPE,
        "message" : GENERIS_RESPONSE_MESSAGE
    }


"""remaining tests are all about response failure - check if can be initialized with an exception"""
def test_response_failure_initialisation_with_exception():
    response = ResponseFailure(GENERIC_RESPONSE_TYPE,Exception("Just an error message"))    


    assert bool(response) is False
    assert response.type == GENERIC_RESPONSE_TYPE
    assert response.message == "Exception: Just an error message"


# """ in order to be able to build a response directly from an invalid request
# and get all the errors that the invalid request contains"""

# def test_response_failure_from_empty_invalid_request():
#     response = build_response_from_invalid_request(RoomListInvalidRequest())

#     assert bool(response) is False
#     assert response.type == ResponseTypes.PARAMETERS_ERROR

# def test_response_failure_from_invalid_request_with_errors():
#     response = RoomListInvalidRequest()
#     response.add_error("path", "Is mandatory")
#     response.add_error("path", "can't be blank")

#     response = build_response_from_invalid_request(response)

#     assert bool(response) is False
#     assert response.type == ResponseTypes.PARAMETERS_ERROR
#     assert response.message == "path: Is mandatory\npath: can't be blank"