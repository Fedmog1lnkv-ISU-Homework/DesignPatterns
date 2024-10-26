from datetime import datetime


class TypeCaster:
    
    __type_to_caster_func = {}
    
    def __init__(self):
        self.__type_to_caster_func = {
            datetime: self.__datetime,
        }
    
    def cast_to_type(self, value, type_to_caste: type):
        if isinstance(value, type_to_caste):
            return value
        
        return self.__internal_caste(value, type_to_caste)
    
    def __internal_caste(self, value, type_to_caste: type):
        if isinstance(value, type_to_caste):
            return value
        
        if isinstance(value, (list, tuple)):
            new_val = []
            for item in value:
                new_val.append(self.__internal_caste(item, type_to_caste))
            return new_val
        
        if type_to_caste in self.__type_to_caster_func:
            caster = self.__type_to_caster_func[type_to_caste]
            return caster(value)
        
        return type_to_caste(value)
    
    @staticmethod
    def __datetime(value):
        if isinstance(value, str):
            return datetime.fromisoformat(value)
        if isinstance(value, int):    
           return datetime.fromtimestamp(value)
        
        return None
        
            