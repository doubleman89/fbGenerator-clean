from dataclasses import dataclass
from typing import ClassVar
from collections.abc import Mapping

from generator.domain.base_entity import DataclassEntity,DataclassEntityWithID

@dataclass
class NetworkTypeCommonDataContainer(DataclassEntity):
    """
    This is dataclass container for:
    - name - network type name 
    - stat variables which are used in network template : dict
    - temp variables which are used in network template : dict
    """
    stat : dict
    temp : dict



@dataclass
class NetworkType(DataclassEntityWithID):
    """
    this is network dataclas, every network class consists of all parameters 
    and corresponding Common Data 
    name - network name - corresponds to tagname
    tags - dictionary of tags generated for every network of this type 
        key - Tag
        Value1 - Tag Type
        Value 2 - Tag Comment
    rows - outer list - refer to number of networks
        - inner list refer to text rows from specific network body  ,
        e.g. one network type can consist of two networs in reality
    """
    instances : ClassVar[dict] = {}
    name : str
    version : str
    comment : str
    tags : dict[str,str]
    rows : list[list]
    commonData : NetworkTypeCommonDataContainer

    def __post_init__(self):
        NetworkType.instances[self.name] = self

    @property
    def commonData(self):
        return self._commonData
    
    @commonData.setter
    def commonData(self,value):
        if isinstance(value,Mapping):
            self._commonData = NetworkTypeCommonDataContainer.from_dict(value)
        elif isinstance(value,NetworkTypeCommonDataContainer):
            self._commonData = value
        else:
            return ValueError(f"wrong value for common data with {value}")


@dataclass
class Network(DataclassEntityWithID):
    networkType : str
    title :str 
    parametersFromParametrizedColumns : dict

    
