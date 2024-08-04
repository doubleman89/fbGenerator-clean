from dataclasses import dataclass
from typing import ClassVar
from collections.abc import Mapping

from generator.domain.base_entity import DataclassEntity,DataclassEntityWithID

@dataclass
class CommonDataContainer(DataclassEntity):
    """
    This is dataclass container for:
    - stat variables which are used in function template : dict
    - temp variables which are used in function template : dict
    
    data are common for all units
    """
    instances : ClassVar[list] =[] 
    stat : dict
    temp : dict

    def __post_init__(self):
        if len(CommonDataContainer.instances) == 0: 
            CommonDataContainer.instances.append(self)
        else:
            pass


@dataclass
class Unit(DataclassEntityWithID):
    """
    This is unit dataclass for:
    - name - unit name 
    - common_data : commonDataContainer
    - temp variables which are used in network template : dict
    """
    instances : ClassVar[dict] ={}
    name : str 
    version : str
    comment : str
    networks : list
    commonData : CommonDataContainer
 

    def __post_init__(self):
        Unit.instances[self.name] = self

    @property
    def commonData(self):
        return self._commonData
    
    @commonData.setter
    def commonData(self,value):
        if isinstance(value,Mapping):
            self._commonData = CommonDataContainer.from_dict(value)
        elif isinstance(value,CommonDataContainer):
            self._commonData = value
        else:
            return ValueError(f"wrong value for common data with {value}")