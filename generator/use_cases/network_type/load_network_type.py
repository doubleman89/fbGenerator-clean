from generator.domain.network import NetworkType
from generator.responses.load_network_type import LoadNetworkTypeResponseFailure,LoadNetworkTypeResponseSuccess
from generator.responses.responses import ResponseTypes


def load_network_type_use_case(request,repo):
    """ loads network type to cache for later use"""
    try:
        repo.update(request.data)
        return LoadNetworkTypeResponseSuccess()
    except Exception as exc:
        return LoadNetworkTypeResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)