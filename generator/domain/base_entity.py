from abc import ABC
from dataclasses import dataclass, asdict
import uuid

@dataclass
class DataclassEntity(ABC):
    
    

    @classmethod
    def from_dict (cls,d):
        return cls(**d)
    
    def to_dict(self):
        return asdict(self)
    
@dataclass
class DataclassEntityWithID(DataclassEntity):
    
    id : uuid.UUID

