from generator.domain.network import NetworkType
from generator.responses.network_type.get_network_type import GetNetworkTypeResponseFailure,GetNetworkTypeResponseSuccess
from generator.responses.responses import ResponseTypes
from generator.responses.responses import build_response_from_invalid_request


def get_network_type_use_case(request,repo):
    if not request :
        return build_response_from_invalid_request(request)
    
    try:
        entity = repo.get(request.data)
        return GetNetworkTypeResponseSuccess(entity)
    except Exception as exc:
        return GetNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)