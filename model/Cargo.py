from datetime import datetime
from typing import List, Any
from helper import Helper


class Cargo:
    timestamp: datetime
    event: str
    vessel: str
    count: int
    inventory: List[Any]

    def __init__(self, timestamp: datetime, event: str, vessel: str, count: int, inventory: List[Any]) -> None:
        self.timestamp = timestamp
        self.event = event
        self.vessel = vessel
        self.count = count
        self.inventory = inventory

    @staticmethod
    def fromDict(obj: Any) -> 'Cargo':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        vessel = Helper.fromString(obj.get("Vessel", ""))
        count = Helper.fromInteger(obj.get("Count", 0))
        inventory = Helper.fromList(lambda x: x, obj.get("Inventory", []))
        return Cargo(timestamp, event, vessel, count, inventory)
