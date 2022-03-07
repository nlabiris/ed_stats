from datetime import datetime
from typing import Any, List
from helper import Helper


class Material:
    name: str
    name_localised: str
    count: int

    def __init__(self, name: str, name_localised: str, count: int) -> None:
        self.name = name
        self.name_localised = name_localised
        self.count = count

    @staticmethod
    def fromDict(obj: Any) -> 'Material':
        assert isinstance(obj, dict)
        name = Helper.fromString(obj.get("Name", ""))
        name_localised = Helper.fromString(obj.get("Name_Localised", ""))
        count = Helper.fromInteger(obj.get("Count", 0))
        return Material(name, name_localised, count)

class Materials:
    timestamp: datetime
    event: str
    raw: List[Material]
    manufactured: List[Material]
    encoded: List[Material]

    def __init__(self, timestamp: datetime, event: str, raw: List[Material], manufactured: List[Material], encoded: List[Material]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.raw = raw
        self.manufactured = manufactured
        self.encoded = encoded

    @staticmethod
    def fromDict(obj: Any) -> 'Materials':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        raw = Helper.fromList(Material.fromDict, obj.get("Raw", []))
        manufactured = Helper.fromList(Material.fromDict, obj.get("Manufactured", []))
        encoded = Helper.fromList(Material.fromDict, obj.get("Encoded", []))
        return Materials(timestamp, event, raw, manufactured, encoded)
