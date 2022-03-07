from datetime import datetime
from typing import Any
from helper import Helper


class MaterialDiscovered:
    timestamp: datetime
    event: str
    category: str
    name: str
    name_localised: str
    discovery_number: int

    def __init__(self, timestamp: datetime, event: str, category: str, name: str, name_localised: str, discovery_number: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.category = category
        self.name = name
        self.name_localised = name_localised
        self.discovery_number = discovery_number

    @staticmethod
    def fromDict(obj: Any) -> 'MaterialDiscovered':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        category = Helper.fromString(obj.get("Category", ""))
        name = Helper.fromString(obj.get("Name", ""))
        name_localised = Helper.fromString(obj.get("Name_Localised", ""))
        discovery_number = Helper.fromInteger(obj.get("DiscoveryNumber", 0))
        return MaterialDiscovered(timestamp, event, category, name, name_localised, discovery_number)
