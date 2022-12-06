import json
from types import SimpleNamespace
from typing import TypeVar, Type, TypedDict
from munch import Munch

T = TypeVar("T")

class Serializer():
    """" Convert json from source represented in strings to object """
    @staticmethod
    def json_to_object(data: str, returnInstance: Type[T]) -> T: 
        return json.loads(data, object_hook=lambda d: SimpleNamespace(**d))

    """  """
    @staticmethod
    def dict_to_object(data: TypedDict, returnInstance: Type[T]) -> T: 
        result = Munch(data)
        return Serializer.json_to_object(result.toJSON(), returnInstance)
