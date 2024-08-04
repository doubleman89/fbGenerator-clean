from generator.domain.network import NetworkType
from generator.responses.network_type.get_network_type import GetNetworkTypeResponseFailure,GetNetworkTypeResponseSuccess
from generator.responses.responses import ResponseTypes


def get_network_type_use_case(request,repo):
    try:
        entity = repo.get(request.data)
        return GetNetworkTypeResponseSuccess(entity)
    except Exception as exc:
        return GetNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)