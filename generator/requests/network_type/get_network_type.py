from dataclasses import dataclass

from generator.requests.requests import ValidRequestObject,GenerateInvalidRequestWithCommonValidation


@dataclass
class GetNetworkTypeInputDto(ValidRequestObject): 
    id : str
    name : str
    version : str


class GetNetworkTypeRequestObject(GetNetworkTypeInputDto):

    @classmethod
    def from_dict(cls, adict):
        
        #generate invalid_req
        invalid_req = GenerateInvalidRequestWithCommonValidation(cls,adict).execute()
        
        if invalid_req.has_errors():
            return invalid_req

        return GetNetworkTypeInputDto(**adict)
