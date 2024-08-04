import pymongo


from generator.repository.mongorepo import MongoRepo
from generator.domain.network import NetworkType

class NetworkTypeMongoRepo(MongoRepo):

    @property
    def collection(self):
        return self.db.networktype
    
    @classmethod
    def entity_object(cls):
        return NetworkType