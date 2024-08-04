from abc import ABC,abstractmethod

class Repo(ABC):
    """Interface class for other repos """
    
    @abstractmethod
    def get(self, entity_id):
        """get entity by id and return entity"""
        raise NotImplementedError
    
    @abstractmethod
    def create(self, data):
        """create specific entity with provided data"""
        raise NotImplementedError
    
    @abstractmethod
    def update(self, entity):
        """ update entity using entity id"""
        return NotImplementedError
    
    


    
