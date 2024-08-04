from dataclasses import dataclass
from typing import ClassVar
from collections.abc import Mapping

from generator.requests.requests import ValidRequestObject,GenerateInvalidRequestWithCommonValidation


@dataclass
class UpdateNetworkTypeInputDto(ValidRequestObject): 
    name : str
    version : str
    comment : str
    tags : dict[str,str]
    rows : list[list]
    common_data : dict[str, dict]

class UpdateNetworkTypeRequestObject(UpdateNetworkTypeInputDto):
    accepted_common_data_fields : ClassVar[set] = {"stat","temp"}

    @classmethod
    def from_dict(cls, adict):
        
        #generate invalid_req
        invalid_req = GenerateInvalidRequestWithCommonValidation(cls,adict).execute()
        
        #check differences between common data
        common_data_diff = cls.accepted_common_data_fields.difference(set(adict["common_data"].keys()))

        if common_data_diff:
            for key in common_data_diff:
                invalid_req.add_error(
                    'common data',
                    'Key {} cannot be used'.format(key)
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
