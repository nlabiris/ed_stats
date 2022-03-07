from datetime import datetime
from typing import Any
from helper import Helper


class FSDTarget:
    timestamp: datetime
    event: str
    name: str
    system_address: int
    star_class: str
    remaining_jumps_in_route: int

    def __init__(self, timestamp: datetime, event: str, name: str, system_address: int, star_class: str, remaining_jumps_in_route: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.name = name
        self.system_address = system_address
        self.star_class = star_class
        self.remaining_jumps_in_route = remaining_jumps_in_route

    @staticmethod
    def fromDict(obj: Any) -> 'FSDTarget':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        name = Helper.fromString(obj.get("Name", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        star_class = Helper.fromString(obj.get("StarClass", ""))
        remaining_jumps_in_route = Helper.fromInteger(obj.get("RemainingJumpsInRoute", 0))
        return FSDTarget(timestamp, event, name, system_address, star_class, remaining_jumps_in_route)
