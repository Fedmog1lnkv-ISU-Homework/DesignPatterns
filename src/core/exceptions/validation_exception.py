from src.core.abstractions.abstract_exception import AbstractException


class ValidationException(AbstractException):
    pass


class TypeValidationException(ValidationException):
    def __init__(self, value, t):
        super().__init__(f'Invalid type, got {type(value)}, waited {t}')


class LengthValidationException(ValidationException):
    def __init__(self, value, length: int):
        super().__init__(f'Invalid length, got {len(value)}, waited {length}')


class FormatValidationException(ValidationException):
    def __init__(self, value, f):
        super().__init__(f'Invalid format, got{value}, waited {f}')
