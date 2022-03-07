from datetime import datetime
from typing import Any
from helper import Helper


class Powerplay:
    timestamp: datetime
    event: str
    power: str
    rank: int
    merits: int
    votes: int
    time_pledged: int

    def __init__(self, timestamp: datetime, event: str, power: str, rank: int, merits: int, votes: int, time_pledged: int) -> None:
        self.timestamp = timestamp
        self.event = event
        self.power = power
        self.rank = rank
        self.merits = merits
        self.votes = votes
        self.time_pledged = time_pledged

    @staticmethod
    def fromDict(obj: Any) -> 'Powerplay':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        power = Helper.fromString(obj.get("Power", ""))
        rank = Helper.fromInteger(obj.get("Rank", 0))
        merits = Helper.fromInteger(obj.get("Merits", 0))
        votes = Helper.fromInteger(obj.get("Votes", 0))
        time_pledged = Helper.fromInteger(obj.get("TimePledged", 0))
        return Powerplay(timestamp, event, power, rank, merits, votes, time_pledged)
