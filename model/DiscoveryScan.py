from datetime import datetime
from typing import Any, TypeVar, Type, cast
from helper import Helper


class DiscoveryScan:
    timestamp: datetime
    event: str
    system_address: int
    bodies: int

    def __init__(self, timestamp: datetime, event: str, system_address: int, bodies: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.system_address = system_address
        self.bodies = bodies

    @staticmethod
    def fromDict(obj: Any) -> 'DiscoveryScan':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        bodies = Helper.fromInteger(obj.get("Bodies", 0))
        return DiscoveryScan(timestamp, event, system_address, bodies)
