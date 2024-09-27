from src.core.abstractions.abstract_exception import AbstractException


class ValueException(AbstractException):
    pass

class NullValueException(ValueException):
    def __init__(self, parameter_name: str):
        super().__init__(f'Invalid value: {parameter_name} cannot be None.')
