import yaml
from typing import TypeVar, Type
from utils.serializer import Serializer

T = TypeVar("T")

class AppConfiguration:

    def loadyaml(self, configFile: str) -> str:
        with open(configFile) as stream: 
            yaml.dump
            return yaml.safe_load(stream)

    def load_yaml_to_object(self, configFile: str, targetObject: Type[T]) -> T:
         a = self.loadyaml(configFile)
         return Serializer.dict_to_object(self.loadyaml(configFile), targetObject)