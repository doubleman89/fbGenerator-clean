from generator.domain.network import NetworkType
from generator.responses.network_type.update_network_type import UpdateNetworkTypeResponseFailure,UpdateNetworkTypeResponseSuccess
from generator.responses.responses import build_response_from_invalid_request
from generator.responses.responses import ResponseTypes


def update_network_type_use_case(request,repo):
    if not request :
        return build_response_from_invalid_request(request)
    try:
        repo.update(request.data)
        return  UpdateNetworkTypeResponseSuccess()
    except Exception as exc:
        return UpdateNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)

    
