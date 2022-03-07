from datetime import datetime
from typing import Any
from helper import Helper


class Rank:
    timestamp: datetime
    event: str
    combat: int
    trade: int
    explore: int
    empire: int
    federation: int
    cqc: int

    def __init__(self, timestamp: datetime, event: str, combat: int, trade: int, explore: int, empire: int, federation: int, cqc: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.combat = combat
        self.trade = trade
        self.explore = explore
        self.empire = empire
        self.federation = federation
        self.cqc = cqc

    @staticmethod
    def fromDict(obj: Any) -> 'Rank':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        combat = Helper.fromInteger(obj.get("Combat", 0))
        trade = Helper.fromInteger(obj.get("Trade", 0))
        explore = Helper.fromInteger(obj.get("Explore", 0))
        empire = Helper.fromInteger(obj.get("Empire", 0))
        federation = Helper.fromInteger(obj.get("Federation", 0))
        cqc = Helper.fromInteger(obj.get("CQC", 0))
        return Rank(timestamp, event, combat, trade, explore, empire, federation, cqc)
