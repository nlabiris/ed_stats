from datetime import datetime
from typing import Any
from helper import Helper

class Commander:
    timestamp: datetime
    event: str
    fid: str
    name: str

    def __init__(self, timestamp: datetime, event: str, fid: str, name: str) -> None:
        self.timestamp = timestamp
        self.event = event
        self.fid = fid
        self.name = name

    @staticmethod
    def fromDict(obj: Any) -> 'Commander':
        assert isinstance(obj, dict)
        timestamp = Helper.fromDatetime(obj.get("timestamp", None))
        event = Helper.fromString(obj.get("event", ""))
        fid = Helper.fromString(obj.get("FID", ""))
        name = Helper.fromString(obj.get("Name", ""))
        return Commander(timestamp, event, fid, name)
