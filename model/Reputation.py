from datetime import datetime
from typing import Any
from helper import Helper


class Reputation:
    timestamp: datetime
    event: str
    empire: float
    federation: float

    def __init__(self, timestamp: datetime, event: str, empire: float, federation: float) -> None:
        self.timestamp = timestamp
        self.event = event
        self.empire = empire
        self.federation = federation

    @staticmethod
    def fromDict(obj: Any) -> 'Reputation':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        empire = Helper.fromFloat(obj.get("Empire", 0))
        federation = Helper.fromFloat(obj.get("Federation", 0))
        return Reputation(timestamp, event, empire, federation)
