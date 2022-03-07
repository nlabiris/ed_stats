from datetime import datetime
from typing import Any
from helper import Helper


class LeaveBody:
    timestamp: datetime
    event: str
    star_system: str
    system_address: int
    body: str
    body_id: int

    def __init__(self, timestamp: datetime, event: str, star_system: str, system_address: int, body: str, body_id: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.star_system = star_system
        self.system_address = system_address
        self.body = body
        self.body_id = body_id

    @staticmethod
    def fromDict(obj: Any) -> 'LeaveBody':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        body = Helper.fromString(obj.get("Body", ""))
        body_id = Helper.fromInteger(obj.get("BodyID", 0))
        return LeaveBody(timestamp, event, star_system, system_address, body, body_id)
