from dataclasses import dataclass
from typing import ClassVar
from collections.abc import Mapping

from generator.requests.requests import ValidRequestObject,GenerateInvalidRequestWithCommonValidation


@dataclass
class LoadNetworkTypeInputDto(ValidRequestObject): 
    name : str
    version : str
    comment : str
    tags : dict[str,str]
    rows : list[list]
    common_data : dict[str, dict]

class LoadNetworkTypeRequestObject(LoadNetworkTypeInputDto):
    accepted_common_data_keys : ClassVar[set] = {"stat","temp"}

    @classmethod
    def from_dict(cls, adict):
        
        #generate invalid_req
        invalid_req = GenerateInvalidRequestWithCommonValidation(cls,adict).execute()
        
        #check differences between common data
        if "common_data" in adict.keys():
            common_data_diff = cls.accepted_common_data_keys.difference(set(adict["common_data"].keys()))
        
            if common_data_diff:
                for key in common_data_diff:
                    if key in cls.accepted_common_data_keys:
                        invalid_req.add_error(
                            'common data',
                            'Field {} is required, but was not included as a parameter'.format(key)
                        )
                    else:
                        invalid_req.add_error(
                            'common data',
                            'Field {} cannot be used'.format(key)
                        )

            for field, value in adict["common_data"].items():
                if not isinstance(value,Mapping):
                    invalid_req.add_error(
                    'common data',
                    'Field {} is not a dictionary'.format(field)
                )

        if invalid_req.has_errors():
            return invalid_req

        return cls(**adict)
