from dataclasses import dataclass
from  dataclass_wizard import JSONSerializable

@dataclass
class Info(JSONSerializable):
    full_name: str
    age : int
    gender: str