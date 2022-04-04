from datetime import datetime
from typing import Any, List
from helper import Helper


class Material:
    name: str
    count: int

    def __init__(self, name: str, count: int) -> None:
        self.name = name
        self.count = count

    @staticmethod
    def fromDict(obj: Any) -> 'Material':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name"))
        count = Helper.fromInteger(obj.get("Count"))
        return Material(name, count)

class Synthesis:
    timestamp: datetime
    event: str
    name: str
    materials: List[Material]

    def __init__(self, timestamp: datetime, event: str, name: str, materials: List[Material]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.name = name
        self.materials = materials

    @staticmethod
    def fromDict(obj: Any) -> 'Synthesis':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        name = Helper.fromString(obj.get("Name", ""))
        materials = Helper.fromList(Material.fromDict, obj.get("Materials", []))
        return Synthesis(timestamp, event, name, materials)
