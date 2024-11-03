from src.core.enums.filter_operation_type import FilterOperationType

class FilterOperationTypeMapper:
    @staticmethod
    def equal(a, b):
        return a == b

    @staticmethod
    def like(a, b):
        return b in a

    @staticmethod
    def between(a, b):
        if not isinstance(b, (list, tuple)):
            return False
        if len(b) != 2:
            return False

        return b[0] < a <= b[1]
    
    __operations_map = {
        FilterOperationType.EQUAL: equal,
        FilterOperationType.LIKE: like,
        FilterOperationType.BETWEEN: between,
    }

    def enum_to_operation(self, operation: FilterOperationType):
        if operation in self.__operations_map.keys():
            return self.__operations_map[operation]

        return FilterOperationTypeMapper.equal
