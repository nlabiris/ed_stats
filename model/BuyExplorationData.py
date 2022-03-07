from datetime import datetime
from typing import Any
from helper import Helper


class BuyExplorationData:
    timestamp: datetime
    event: str
    system: str
    cost: int

    def __init__(self, timestamp: datetime, event: str, system: str, cost: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.system = system
        self.cost = cost

    @staticmethod
    def fromDict(obj: Any) -> 'BuyExplorationData':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        system = Helper.fromString(obj.get("System", ""))
        cost = Helper.fromInteger(obj.get("Cost", 0))
        return BuyExplorationData(timestamp, event, system, cost)
