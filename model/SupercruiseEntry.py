from datetime import datetime
from typing import Any
from helper import Helper


class SupercruiseEntry:
    timestamp: datetime
    event: str
    star_system: str
    system_address: int

    def __init__(self, timestamp: datetime, event: str, star_system: str, system_address: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.star_system = star_system
        self.system_address = system_address

    @staticmethod
    def fromDict(obj: Any) -> 'SupercruiseEntry':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        star_system = Helper.fromString(obj.get("StarSystem", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        return SupercruiseEntry(timestamp, event, star_system, system_address)
