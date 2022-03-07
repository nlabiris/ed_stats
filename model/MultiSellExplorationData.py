from datetime import datetime
from typing import Any, List
from helper import Helper


class Discovered:
    system_name: str
    num_bodies: int

    def __init__(self, system_name: str, num_bodies: int) -> None:
        self.system_name = system_name
        self.num_bodies = num_bodies

    @staticmethod
    def fromDict(obj: Any) -> 'Discovered':
        assert isinstance(obj, dict)
        system_name = Helper.fromString(obj.get("SystemName", ""))
        num_bodies = Helper.fromInteger(obj.get("NumBodies", 0))
        return Discovered(system_name, num_bodies)

class MultiSellExplorationData:
    timestamp: datetime
    event: str
    discovered: List[Discovered]
    base_value: int
    bonus: int
    total_earnings: int

    def __init__(self, timestamp: datetime, event: str, discovered: List[Discovered], base_value: int, bonus: int, total_earnings: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.discovered = discovered
        self.base_value = base_value
        self.bonus = bonus
        self.total_earnings = total_earnings

    @staticmethod
    def fromDict(obj: Any) -> 'MultiSellExplorationData':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        discovered = Helper.fromList(Discovered.fromDict, obj.get("Discovered", []))
        base_value = Helper.fromInteger(obj.get("BaseValue", 0))
        bonus = Helper.fromInteger(obj.get("Bonus", 0))
        total_earnings = Helper.fromInteger(obj.get("TotalEarnings", 0))
        return MultiSellExplorationData(timestamp, event, discovered, base_value, bonus, total_earnings)
