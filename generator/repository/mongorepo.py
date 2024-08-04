import pymongo
from abc import abstractmethod

from generator.repository.repo import Repo



def convert_results_to_entity_dict(results_dict):
    entity_dict = {}
    for key, value in results_dict.items():
        if "_id" == key:
            entity_dict["id"]  = results_dict["_id"]
            continue
        entity_dict[key]  = results_dict[value]
    return entity_dict

class MongoRepo(Repo):
    """ interface class for all Mongo Repos """
    def __init__(self,app_configuration) -> None:
        client = pymongo.MongoClient(
        host = app_configuration["MONGODB_HOSTNAME"],
        port = int(app_configuration["MONGODB_PORT"]),
        username = app_configuration["MONGODB_USER"],
        password = app_configuration["MONGODB_PASSWORD"],
        authSource = "admin",
        )

        self.db = client[app_configuration["APPLICATION_DB"]]
    
    @abstractmethod
    @property
    def collection(self):
        raise NotImplementedError
    
    @abstractmethod
    @classmethod
    def entity_object(cls):
        raise NotImplementedError

    def get(self, entity_id):
        """get entity by id and return entity"""
        collection = self.collection()
        entity_object = __class__.entity_object()

        result = collection.find({"_id":entity_id})[0]
        
        return entity_object.from_dict(convert_results_to_entity_dict(result))

    
    def create(self, entities):
        """create specific entity with provided data"""
        collection = self.collection()

        collection.insert_many([

            {entity.to_dict()}
            for entity in entities
            
            ] 
        )

        
     
    def update(self, entity):
        """ update entity using entity id"""
        collection = self.collection()
        
        collection.update_one(
            {"_id":entity.id},
            {"$set" : entity.to_dict()}
            )
    
    def _create_entity_objects(self,result):

        entity_object = __class__.entity_object()

        return [
            entity_object.from_dict(convert_results_to_entity_dict(q))
            for q in result
        ]

    def list(self,filters = None, keys_to_int = None):
        """query entities with filters"""
        collection = self.collection()

        if filters is None:
            result = collection.find()
        else:
            mongo_filter ={}
            for key,value in filters.items():
                key,operator = key.split("__")

                filter_value = mongo_filter.get(key,{})

                if keys_to_int is None :
                    pass
                elif key in keys_to_int:
                    value = int(value)

                filter_value["${}".format(operator)] = value
                mongo_filter[key] = filter_value

            result = collection.find(mongo_filter)
        
        return self._create_entity_objects(result)
    