from datetime import datetime
from typing import Any, List
from helper import Helper


class SellExplorationData:
    timestamp: datetime
    event: str
    systems: List[str]
    discovered: List[str]
    base_value: int
    bonus: int
    total_earnings: int

    def __init__(self, timestamp: datetime, event: str, systems: List[str], discovered: List[str], base_value: int, bonus: int, total_earnings: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.systems = systems
        self.discovered = discovered
        self.base_value = base_value
        self.bonus = bonus
        self.total_earnings = total_earnings

    @staticmethod
    def fromDict(obj: Any) -> 'SellExplorationData':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        systems = Helper.fromList(Helper.fromString, obj.get("Systems", []))
        discovered = Helper.fromList(Helper.fromString, obj.get("Discovered", []))
        base_value = Helper.fromInteger(obj.get("BaseValue", 0))
        bonus = Helper.fromInteger(obj.get("Bonus", 0))
        total_earnings = Helper.fromInteger(obj.get("TotalEarnings", 0))
        return SellExplorationData(timestamp, event, systems, discovered, base_value, bonus, total_earnings)
