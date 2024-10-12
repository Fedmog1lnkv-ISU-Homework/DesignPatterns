from src.core.enums.filter_operation_type import FilterOperationType

def equal(a, b):
    return a == b


def like(a, b):
    return b in a


class FilterOperationTypeMapper:
    __operations_map = {
        FilterOperationType.EQUAL: equal,
        FilterOperationType.LIKE: like,
    }

    def enum_to_operation(self, operation: FilterOperationType):
        if operation in self.__operations_map.keys():
            return self.__operations_map[operation]

        return equal