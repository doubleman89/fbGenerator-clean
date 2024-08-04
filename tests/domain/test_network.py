import pytest

from generator.domain.network import Network, NetworkType
from tests.domain.entity_examples import networks, network_types

len_networks = len(networks)
len_network_types = len(network_types)

@pytest.mark.parametrize("iteration", range(len_networks))
def test_network_model_init(iteration ):
    network_dict = networks[iteration]
    network1 = Network.from_dict(network_dict)
    network2 = Network.from_dict(network_dict)

    assert network1.to_dict() == network_dict
    assert network1 == network2

@pytest.mark.parametrize("iteration", range(len_network_types))
def test_network_type_init(iteration ):
    network_types_dict = network_types[iteration]
    network1 = NetworkType.from_dict(network_types_dict)
    network2 = NetworkType.from_dict(network_types_dict)

    assert network1.to_dict() == network_types_dict
    assert network1 == network2

    