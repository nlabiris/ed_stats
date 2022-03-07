from datetime import datetime
from typing import Any
from helper import Helper


class MaterialCollected:
    timestamp: datetime
    event: str
    category: str
    name: str
    name_localised: str
    count: int

    def __init__(self, timestamp: datetime, event: str, category: str, name: str, name_localised: str, count: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.category = category
        self.name = name
        self.name_localised = name_localised
        self.count = count

    @staticmethod
    def fromDict(obj: Any) -> 'MaterialCollected':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        category = Helper.fromString(obj.get("Category", ""))
        name = Helper.fromString(obj.get("Name", ""))
        name_localised = Helper.fromString(obj.get("Name_Localised", ""))
        count = Helper.fromInteger(obj.get("Count", 0))
        return MaterialCollected(timestamp, event, category, name, name_localised, count)
