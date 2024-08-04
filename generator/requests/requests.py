from types import GenericAlias

from dataclasses import _MISSING_TYPE as missing_type 



class InvalidRequestObject:
    def __init__(self) -> None:
        self.errors = []
    

    def __bool__(self):
        return False


    def add_error(self,parameter,message):
        self.errors.append({"parameter": parameter, "message":message})
    

    def has_errors(self):
        return len(self.errors) > 0


class ValidRequestObject:
    
    def __bool__(self):
        return True
    

    @classmethod
    def from_dict(cls, adict):
        raise NotImplementedError


class GenerateInvalidRequestWithCommonValidation:

    def __init__(self,validated_class, dictionary_for_object_generation) -> None:
        self.validated_class = validated_class
        self.dictionary_for_object_generation = dictionary_for_object_generation


    def execute(self) -> InvalidRequestObject :
        
        invalid_req = InvalidRequestObject()

        # get dataclass fields
        required_fields, init_fields, field_types = self._get_dataclass_fields_info()
        
        #check if there are some wrong or missing fields
        missing_fields,wrong_fields,incorrect_field_types = self._compare_fields_with_dict(required_fields, init_fields,field_types)
        
        #add errors for fields with wrong parametery type
        for field,type in incorrect_field_types.items():
            invalid_req.add_error(field, f'Field {field} has a wrong parameter type. It was declared as {type.__name__}, but it should be {field_types[field].__name__}')

        # if there are some wrong or missing fields, add messages 
        if len(missing_fields) > 0 : 
            for key in missing_fields:
                invalid_req.add_error(key, f'Field {key} is required, but was not included as a parameter')
        
        if len(wrong_fields) > 0 : 
            for key in wrong_fields:
                invalid_req.add_error(key, f'Field {key} does not belong to the parameters')
        
        return invalid_req


    def _get_dataclass_fields_info(self):
        """
        get required fields ,all init fields and fields types
        """
        required_fields =[]
        init_fields = []
        field_types = {}

        for key, value in self.validated_class.__dataclass_fields__.items():

            if not value.init:
                continue
            
            init_fields.append(key)

            if isinstance(value.default,missing_type) :
                required_fields.append(key)
            
            if isinstance(value.type,GenericAlias):
                field_types[key] = value.type.__origin__
            else:
                field_types[key] = value.type
                       
        return required_fields, init_fields,field_types
    

    def _compare_fields_with_dict(self,required_fields, init_fields,field_types):
        """
        compare required  and all init fields with the provided dict 
        return: 
        missing fields - required fields missing
        wrong fields - fields that does not belong to all init fields 
        wrong

        """
        wrong_fields =[]
        missing_fields = required_fields
        incorrect_field_types = {}

        dic = self.dictionary_for_object_generation

        for key,value  in dic.items():

            if key not in init_fields:
                wrong_fields.append(key)
                continue

            if key in required_fields:
                missing_fields.remove(key)

            if not isinstance(value,field_types[key]): 
                incorrect_field_types[key] = type(value)
                        
        return missing_fields,wrong_fields, incorrect_field_types
    



        
    

        






    


