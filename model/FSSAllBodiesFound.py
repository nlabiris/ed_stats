from datetime import datetime
from typing import Any
from helper import Helper


class FSSAllBodiesFound:
    timestamp: datetime
    event: str
    system_name: str
    system_address: int
    count: int

    def __init__(self, timestamp: datetime, event: str, system_name: str, system_address: int, count: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.system_name = system_name
        self.system_address = system_address
        self.count = count

    @staticmethod
    def fromDict(obj: Any) -> 'FSSAllBodiesFound':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        system_name = Helper.fromString(obj.get("SystemName", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        count = Helper.fromInteger(obj.get("Count", 0))
        return FSSAllBodiesFound(timestamp, event, system_name, system_address, count)
