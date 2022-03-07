from datetime import datetime
from typing import Any
from helper import Helper


class NavBeaconScan:
    timestamp: datetime
    event: str
    system_address: int
    num_bodies: int

    def __init__(self, timestamp: datetime, event: str, system_address: int, num_bodies: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.system_address = system_address
        self.num_bodies = num_bodies

    @staticmethod
    def fromDict(obj: Any) -> 'NavBeaconScan':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        system_address = Helper.fromInteger(obj.get("SystemAddress", 0))
        num_bodies = Helper.fromInteger(obj.get("NumBodies", 0))
        return NavBeaconScan(timestamp, event, system_address, num_bodies)
