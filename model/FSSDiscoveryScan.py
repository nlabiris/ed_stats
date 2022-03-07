from datetime import datetime
from typing import Any
from helper import Helper


class FSSDiscoveryScan:
    timestamp: datetime
    event: str
    progress: float
    body_count: int
    non_body_count: int
    system_name: str
    system_address: int

    def __init__(self, timestamp: datetime, event: str, progress: float, body_count: int, non_body_count: int, system_name: str, system_address: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.progress = progress
        self.body_count = body_count
        self.non_body_count = non_body_count
        self.system_name = system_name
        self.system_address = system_address

    @staticmethod
    def fromDict(obj: Any) -> 'FSSDiscoveryScan':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        progress = Helper.fromFloat(obj.get("Progress", 0))
        body_count = Helper.fromInteger(obj.get("BodyCount", 0))
        non_body_count = Helper.fromInteger(obj.get("NonBodyCount", 0))
        system_name = Helper.fromString(obj.get("SystemName", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        return FSSDiscoveryScan(timestamp, event, progress, body_count, non_body_count, system_name, system_address)
