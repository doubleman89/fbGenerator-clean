from generator.responses.network_type.create_network_type import CreateNetworkTypeResponseFailure,CreateNetworkTypeResponseSuccess
from generator.responses.responses import ResponseTypes
from generator.responses.responses import build_response_from_invalid_request


def create_network_type_use_case(request,repo):
    """ creates network type to cache for later use"""
    
    if not request :
        return build_response_from_invalid_request(request)
    
    try:
        repo.create([request])
        return CreateNetworkTypeResponseSuccess()
    except Exception as exc:
        return CreateNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
    
def create_network_types_use_case(requests,repo):
    """ creates network types to cache for later use"""

    for request in requests:
        if not request :
            return build_response_from_invalid_request(request)
    try:
        repo.create(requests)
        return CreateNetworkTypeResponseSuccess()
    except Exception as exc:
        return CreateNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)